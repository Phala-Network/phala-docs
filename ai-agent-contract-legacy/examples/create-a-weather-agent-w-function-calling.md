# Create a Weather Agent w/ Function Calling

{% hint style="info" %}
View the example code [here](https://github.com/HashWarlock/ai-agent-template-hello). The code is based on the [guide](https://cookbook.openai.com/examples/how\_to\_build\_an\_agent\_with\_the\_node\_sdk) on how to build an agent from the OpenAI Cookbook.
{% endhint %}

## Overview

In this tutorial, you will learn how to create an agent with 2 functions to enable [function calling](https://platform.openai.com/docs/guides/function-calling) for your agent. The 2 functions we will implement are:

* `getLocation()`  - Get the current location (latitude, longitude) based on the IP of the worker node if no location is described in the user prompt.
* `getWeatherData(latitude, longitude)` - Get the current weather data based on the latitude and longitude retrieved from `getLocation()`.&#x20;

These two functions will be described for your agent to understand the purpose of the functions. Then we will set the system prompt for the agent with:

```
You are a helpful assistant. Only use the functions you have been provided with.
```

## Getting Started

### Prepare

Clone git repo or use [degit](https://www.npmjs.com/package/degit) to get the source code.

{% tabs %}
{% tab title="git" %}
```sh
git clone https://github.com/Phala-Network/ai-agent-template-openai.git
```
{% endtab %}

{% tab title="degit" %}
```sh
npx degit github:Phala-Network/ai-agent-template-openai#main ai-agent-template-openai
```
{% endtab %}
{% endtabs %}

Install dependencies

```
npm install
```

## Creating Your Functions

In this step, we will create our 2 functions `getLocation()` and `getWeatherData(latitude, longitude)` then we will describe our functions for the agent to understand how to use the functions.

Go to your `src/index.ts` file, your initial file should look like the following.

<details>

<summary>src/index.ts</summary>

```typescript
import { Request, Response, route } from './httpSupport'
import { renderHtml } from './uiSupport'

import OpenAI from 'openai'

async function GET(req: Request): Promise<Response> {
    const secret = req.queries?.key ?? '';
    const openaiApiKey = req.secret?.openaiApiKey as string;
    const openai = new OpenAI({ apiKey: openaiApiKey })
    const query = req.queries.chatQuery[0] as string;

    const completion = await openai.chat.completions.create({
        messages: [{ role: "system", content: `${query}` }],
        model: 'gpt-3.5-turbo',
    });

    return new Response(renderHtml(completion.choices[0].message.content as string))
}

async function POST(req: Request): Promise<Response> {
    const secret = req.queries?.key ?? '';
    const openaiApiKey = req.secret?.openaiApiKey as string;
    const openai = new OpenAI({ apiKey: openaiApiKey })
    const query = req.queries.chatQuery[0] as string;

    const completion = await openai.chat.completions.create({
        messages: [{ role: "system", content: `${query}` }],
        model: 'gpt-3.5-turbo',
    });

    return new Response(renderHtml(completion.choices[0].message.content as string))
}

export default async function main(request: string) {
    return await route({ GET, POST }, request)
}
```

</details>

### Create getLocation()

For the `getLocation()` function, we will need to call an API to get the location based on [https://ipapi.co/](https://ipapi.co/). Traditionally, devs will not have access to the internet, but with Phala's AI Agent Contracts, devs now can make async HTTP calls to bring more data for fine tuning their agents.&#x20;

The implementation is simple and we will add this following code.

```typescript
async function getLocation() {
    const response = await fetch("https://ipapi.co/json/");
    const locationData = await response.json();
    return locationData;
}
```

### Create getWeatherData(latitude, longitude)

For the getWeatherData(latitude, longitude) function, we will call the free weather API by [https://open-meteo.com/](https://open-meteo.com/).&#x20;

We will add the following code to our `index.ts` file.

```typescript
async function getCurrentWeather(latitude: any, longitude: any) {
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=apparent_temperature`;
    const response = await fetch(url);
    const weatherData = await response.json();
    return weatherData;
}
```

### Describe Functions

For our OpenAI agent to understand the purpose of these functions, we need to describe them using a specific schema. We'll create an array called `tools` that contains one object per function. Each object will have two keys: `type`, `function`, and the `function` key has three subkeys: `name`, `description`, and `parameters`.

```typescript
const tools = [
    {
        type: "function",
        function: {
            name: "getCurrentWeather",
            description: "Get the current weather in a given location",
            parameters: {
                type: "object",
                properties: {
                    latitude: {
                        type: "string",
                    },
                    longitude: {
                        type: "string",
                    },
                },
                required: ["longitude", "latitude"],
            },
        }
    },
    {
        type: "function",
        function: {
            name: "getLocation",
            description: "Get the user's location based on their IP address",
            parameters: {
                type: "object",
                properties: {},
            },
        }
    },
];

const availableTools = {
    getCurrentWeather,
    getLocation,
};
```

## Add Agent Functionality

### Setup Messages for Agent

We need to define a `messages` array. This will keep track of all of the messages back and forth between our app and OpenAI. Here we create a type `MessageInfo` that will be the fields that may be included in the `messages` array.

The first object in the array should always have the `role` property set to `"system"`, which tells OpenAI that this is how we want it to behave.

```typescript
type MessageInfo = {
    role: any,
    content: any,
    name?: any,
}

const messages: MessageInfo[] = [
    {
        role: "system",
        content: `You are a helpful assistant. Only use the functions you have been provided with.`,
    },
];
```

### Create Agent Function For User Input

We are now ready to build the logic of our app, which lives in the `agent` function. It is asynchronous and takes one argument: the `userInput`.

We start by pushing the `userInput` to the messages array. This time, we set the `role` to `"user"`, so that OpenAI knows that this is the input from the user.

```typescript
async function agent(openai, userInput) {
  messages.push({
    role: "user",
    content: userInput,
  });
  const response = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: messages,
    tools: tools,
  });
  console.log(response);
}
```

Next, we'll send a request to the Chat completions endpoint via the `chat.completions.create()` method in the Node SDK. This method takes a configuration object as an argument. In it, we'll specify three properties:

* `model` - Decides which AI model we want to use (in our case, GPT-4).
* `messages` - The entire history of messages between the user and the AI up until this point.
* `tools` - A list of tools the model may call. Currently, only functions are supported as a tool., we'll we use the `tools` array we created earlier.

### Turn OpenAI Agent Response into Functions

Now that we have the name of the function as a string, we'll need to translate that into a function call. To help us with that, we'll gather both of our functions in an object called `availableTools`:

```typescript
const availableTools = {  getCurrentWeather,  getLocation,};
```

This is handy because we'll be able to access the `getLocation` function via bracket notation and the string we got back from OpenAI, like this: `availableTools["getLocation"]`.

```typescript
const { finish_reason, message } = response.choices[0]; 
if (finish_reason === "tool_calls" && message.tool_calls) {  
    const functionName = message.tool_calls[0].function.name;  
    const functionToCall = availableTools[functionName];  
    const functionArgs = JSON.parse(message.tool_calls[0].function.arguments);  
    const functionArgsArr = Object.values(functionArgs);  
    const functionResponse = await functionToCall.apply(null, functionArgsArr);  
    console.log(functionResponse);
}
```

We're also grabbing ahold of any arguments OpenAI wants us to pass into the function: `message.tool_calls[0].function.arguments`. However, we won't need any arguments for this first function call.

If we run the code again with the same input (`"Where am I located right now?"`), we'll see that `functionResponse` is an object filled with location about where the user is located right now. In my case, that is Oslo, Norway.

```bash
{ip: "193.212.60.170", network: "193.212.60.0/23", version: "IPv4", city: "Oslo", region: "Oslo County", region_code: "03", country: "NO", country_name: "Norway", country_code: "NO", country_code_iso3: "NOR", country_capital: "Oslo", country_tld: ".no", continent_code: "EU", in_eu: false, postal: "0026", latitude: 59.955, longitude: 10.859, timezone: "Europe/Oslo", utc_offset: "+0200", country_calling_code: "+47", currency: "NOK", currency_name: "Krone", languages: "no,nb,nn,se,fi", country_area: 324220, country_population: 5314336, asn: "AS2119", org: "Telenor Norge AS"}
```

We'll add this data to a new item in the `messages` array, where we also specify the name of the function we called.

```typescript
messages.push({
  role: "function",
  name: functionName,
  content: `The result of the last function was this: ${JSON.stringify(
    functionResponse
  )}
  `,
});
```

Notice that the `role` is set to `"function"`. This tells OpenAI that the `content` parameter contains the result of the function call and not the input from the user.

At this point, we need to send a new request to OpenAI with this updated `messages` array. However, we don’t want to hard code a new function call, as our agent might need to go back and forth between itself and GPT several times until it has found the final answer for the user.

This can be solved in several different ways, e.g. recursion, a while-loop, or a for-loop. We'll use a good old for-loop for the sake of simplicity.&#x20;

### Creating The Loop

At the top of the `agent` function, we'll create a loop that lets us run the entire procedure up to five times.

If we get back `finish_reason: "tool_calls"` from GPT, we'll just push the result of the function call to the `messages` array and jump to the next iteration of the loop, triggering a new request.

If we get `finish_reason: "stop"` back, then GPT has found a suitable answer, so we'll return the function and cancel the loop.

```typescript
for (let i = 0; i < 5; i++) {
  const response = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: messages,
    tools: tools,
  });
  const { finish_reason, message } = response.choices[0];
 
  if (finish_reason === "tool_calls" && message.tool_calls) {
    const functionName = message.tool_calls[0].function.name;
    const functionToCall = availableTools[functionName];
    const functionArgs = JSON.parse(message.tool_calls[0].function.arguments);
    const functionArgsArr = Object.values(functionArgs);
    const functionResponse = await functionToCall.apply(null, functionArgsArr);
 
    messages.push({
      role: "function",
      name: functionName,
      content: `
          The result of the last function was this: ${JSON.stringify(
            functionResponse
          )}
          `,
    });
  } else if (finish_reason === "stop") {
    messages.push(message);
    return message.content;
  }
}
return "The maximum number of iterations has been met without a suitable answer. Please try again with a more specific input.";
```

If we don't see a `finish_reason: "stop"` within our five iterations, we'll return a message saying we couldn’t find a suitable answer.

## Update GET() and POST()

Now we need to call our `agent(openai, userInput)` in our `GET` and `POST` calls that will pass in a users prompt that can be accessed in the `chatQuery` property. The code change is minimal and our functions look like the following.

```typescript
async function GET(req: Request): Promise<Response> {
    const secret = req.queries?.key ?? '';
    const openaiApiKey = req.secret?.openaiApiKey as string;
    const openai = new OpenAI({ apiKey: openaiApiKey })
    const query = req.queries.chatQuery[0] as string;

    const response = await agent(openai, query);

    return new Response(renderHtml(response as string))
}

async function POST(req: Request): Promise<Response> {
    const secret = req.queries?.key ?? '';
    const openaiApiKey = req.secret?.openaiApiKey as string;
    const openai = new OpenAI({ apiKey: openaiApiKey })
    const query = req.queries.chatQuery[0] as string;

    const response = await agent(openai, query);

    return new Response(renderHtml(response as string))
}
```

## Test Locally

Now that we have the code implemented to interact with APIs and call the functions, let's test the code locally.

Create `.env` file with the default ThirdWeb API key for publishing your Agent Contract to IPFS

```
cp .env.local .env
```

In `./secrets/default.json` file replace `YOUR_OPENAI_KEY` with your API Key

```json
{
  "openaiApiKey": "YOUR_OPENAI_API_KEY"
}
```

> In your `./tests/test.ts` file. Add your API Key manually to have a functional test.
>
> ```typescript
> let getResult = await execute({
>     method: 'GET',
>     path: '/ipfs/CID',
>     queries: { chatQuery: ["Who are you?"] },
>     secret: { openaiApiKey: "YOUR_OPENAI_API_KEY" },
>     headers: {},
> })
> ```

Build your Agent

```
npm run build
```

Test your Agent locally

```
npm run test
```

Expected output:

```bash
INPUT: {"method":"GET","path":"/ipfs/CID","queries":{},"secret":{"openaiApiKey":"OPENAI_API_KEY"},"headers":{}}
[0]chat
[1]chat
[2]chat
GET RESULT: {
  status: 200,
  body: `{"message":"There's a lot to do in Austin, Texas! Here are some activities you might consider based on the current weather and various interests:\\n\\n### Outdoor Activities\\n1. **Lady Bird Lake & Zilker Park**\\n   - **Kayaking/Paddleboarding**: Enjoy a relaxing paddle on Lady Bird Lake.\\n   - **Hiking/Biking**: Explore the trails around Zilker Park and Barton Springs.\\n\\n2. **Barton Springs Pool**\\n   - A perfect spot for a swim and to cool off from the summer heat.\\n\\n3. **Mount Bonnell**\\n   - For those who love scenic views and a bit of hiking, head to Mount Bonnell for a panoramic view of the city.\\n\\n### Cultural Activities\\n1. **Blanton Museum of Art**\\n   - Explore a variety of art collections ranging from contemporary to ancient.\\n\\n2. **Bullock Texas State History Museum**\\n   - Learn about the rich history of Texas through exhibits and films.\\n\\n3. **South Congress Avenue (SoCo)**\\n   - Wander through boutique shops, galleries, and enjoy some street performances.\\n\\n### Music & Nightlife\\n1. **Live Music**\\n   - Check out iconic venues like the Continental Club or Antone’s for some live performances.\\n\\n2. **Rainey Street Historic District**\\n   - Explore a variety of bars and food trucks in this lively area.\\n\\n### Food & Beverage\\n1. **BBQ Heaven**\\n   - Visit Franklin Barbecue or la Barbecue for some of the best BBQ in the city.\\n   \\n2. **Food Trucks**\\n   - Explore the diverse array of food trucks offering a variety of cuisines.\\n\\n### Weather Considerations\\n- The apparent temperature during the day can reach up to 37.2°C (98.96°F) with some moments going as high as 38.9°C (102.02°F). Ensure you stay hydrated and take breaks in shaded or air-conditioned areas.\\n\\nNo matter what your interests are, Austin has a variety of activities to make your day enjoyable. Make sure to check local event listings as well for any special events or festivals happening today."}`,
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  }
}
INPUT: {"method":"GET","path":"/ipfs/CID","queries":{"chatQuery":["What are some activities based in Brussels today?"]},"secret":{"openaiApiKey":"OPENAI_API_KEY"},"headers":{}}
[0]chat
[1]chat
[2]chat
[3]chat
GET RESULT: {
  status: 200,
  body: `{"message":"Brussels is a vibrant city with a lot of things to offer on any given day. Here are some activities you can enjoy today:\\n\\n### Outdoor Activities\\n1. **Grand Place**\\n   - Visit the heart of Brussels and marvel at the stunning architecture. You might catch some street performances as well.\\n\\n2. **Parc du Cinquantenaire**\\n   - Take a relaxing stroll or have a picnic in this beautiful park.\\n\\n3. **Atomium**\\n   - Explore this unique building and enjoy panoramic views of the city.\\n\\n### Cultural Activities\\n1. **Royal Museums of Fine Arts of Belgium**\\n   - Explore Belgian art and various exhibitions ranging from ancient to modern art.\\n\\n2. **Magritte Museum**\\n   - Dive into the surreal world of René Magritte, one of Belgium's most famous artists.\\n\\n3. **Belgian Comic Strip Center**\\n   - Discover the rich history of comic strips in Belgium, including famous characters like Tintin.\\n\\n### Gourmet Experiences\\n1. **Chocolate and Beer Tours**\\n   - Take a guided tour to sample some of Brussels' best chocolates and beers.\\n\\n2. **Waffles and Frites**\\n   - Enjoy traditional Belgian waffles and fries at local eateries.\\n\\n### Shopping and Markets\\n1. **Galeries Royales Saint-Hubert**\\n   - Explore this beautiful shopping arcade filled with boutique shops and cafes.\\n\\n2. **Marolles Flea Market**\\n   - Hunt for unique items and antiques at this bustling market.\\n\\n### Theatre and Music\\n1. **Ancienne Belgique**\\n   - Check out the schedule for any concerts or performances happening today.\\n\\n2. **La Monnaie/De Munt**\\n   - Attend an opera or a ballet performance if available.\\n\\n### Historical Sites\\n1. **Manneken Pis**\\n   - Visit this famous statue, which often gets dressed up in various costumes.\\n\\n2. **Palais de Justice**\\n   - Visit this impressive courthouse and enjoy the views from its location.\\n\\n### Weather Considerations\\n- The apparent temperature in Brussels today ranges from 15.9°C (60.62°F) in the early morning to a high of around 31.6°C (88.88°F) in the late afternoon. Thus, it is quite pleasant for outdoor activities.\\n\\nWhatever your interests, Brussels has something to offer for everyone. Make sure to check local event listings as well for any special events or festivals happening today. Enjoy your day!"}`,
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  }
}
Now you are ready to publish your agent, add secrets, and interact with your agent in the following steps:
- Execute: 'npm run publish-agent'
- Set secrets: 'npm run set-secrets'
- Go to the url produced by setting the secrets (e.g. https://wapo-testnet.phala.network/ipfs/QmPQJD5zv3cYDRM25uGAVjLvXGNyQf9Vonz7rqkQB52Jae?key=b092532592cbd0cf)
```

## Publish & Interact with Agent

With our test passing and everything working as expected, now we can build and publish our agent code to IPFS. Then we will set our secrets and access our deployed agent via the Phala Gateway at https://wapo-testnet.phala.network/ipfs/\<cid>?key=\<key\_id>\&chatQuery=\<chat\_query>.

Upload your compiled AI Agent code to IPFS.

```bash
npm run publish-agent
```

Upon a successful upload, the command should show the URL to access your AI Agent.

```
✓ Compiled successfully.
  78.19 KB  dist/index.js
Running command: npx thirdweb upload dist/index.js
This may require you to log into thirdweb and will take some time to publish to IPFS...

    $$\     $$\       $$\                 $$\                         $$\       
    $$ |    $$ |      \__|                $$ |                        $$ |      
  $$$$$$\   $$$$$$$\  $$\  $$$$$$\   $$$$$$$ |$$\  $$\  $$\  $$$$$$\  $$$$$$$\  
  \_$$  _|  $$  __$$\ $$ |$$  __$$\ $$  __$$ |$$ | $$ | $$ |$$  __$$\ $$  __$$\ 
    $$ |    $$ |  $$ |$$ |$$ |  \__|$$ /  $$ |$$ | $$ | $$ |$$$$$$$$ |$$ |  $$ |
    $$ |$$\ $$ |  $$ |$$ |$$ |      $$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |  $$ |
    \$$$$  |$$ |  $$ |$$ |$$ |      \$$$$$$$ |\$$$$$\$$$$  |\$$$$$$$\ $$$$$$$  |
     \____/ \__|  \__|\__|\__|       \_______| \_____\____/  \_______|\_______/ 

 💎 thirdweb v0.14.12 💎

- Uploading file to IPFS. This may take a while depending on file sizes.

✔ Successfully uploaded file to IPFS.
✔ Files stored at the following IPFS URI: ipfs://QmQZYAkEz8RnX9phpWscDLsv1u7uBATaAYHb1prpFGvD4n
✔ Open this link to view your upload: https://b805a9b72767504353244e0422c2b5f9.ipfscdn.io/ipfs/bafybeibbasdv4xt32ea74ga77rpr5kgnkxcgqbtoslgxagzhmmujcjwkym/

Agent Contract deployed at: https://wapo-testnet.phala.network/ipfs/QmQZYAkEz8RnX9phpWscDLsv1u7uBATaAYHb1prpFGvD4n

If your agent requires secrets, ensure to do the following:
1) Edit the ./secrets/default.json file or create a new JSON file in the ./secrets folder and add your secrets to it.
2) Run command: 'npm run set-secrets' or 'npm run set-secrets [path-to-json-file]'
Logs folder created.
Deployment information updated in ./logs/latestDeployment.json
```

{% hint style="info" %}
**Note** that your latest deployment information will be logged to in file [`./logs/latestDeployment.json`](https://github.com/Phala-Network/ai-agent-template-func-calling/blob/main/logs/latestDeployment.json). This file is updated every time you publish a new Agent Contract to IPFS. This file is also used to get the IPFS CID of your Agent Contract when setting secrets for your Agent Contract.

Here is an example:

```
{
  "date": "2024-08-29T20:28:20.081Z",
  "cid": "QmYzBTdQNPewdhD9GdBJ9TdV7LVhrh9YVRiV8aBup7qZGu",
  "url": "https://wapo-testnet.phala.network/ipfs/QmYzBTdQNPewdhD9GdBJ9TdV7LVhrh9YVRiV8aBup7qZGu"
}
```
{% endhint %}

{% hint style="warning" %}
**Did Thirdweb fail to publish?**

If ThirdWeb fails to publish, please signup for your own ThirdWeb account to publish your Agent Contract to IPFS. Signup or login at [https://thirdweb.com/dashboard/](https://thirdweb.com/dashboard/)

Whenever you log into ThirdWeb, create a new API key and replace the default API Key with yours in the [.env](https://github.com/Phala-Network/ai-agent-template-func-calling/blob/main/.env) file.\
`THIRDWEB_API_KEY="YOUR_THIRDWEB_API_KEY"`
{% endhint %}

### Add Secrets

By default, all the compiled JS code is visible for anyone to view if they look at IPFS CID. This makes private info like API keys, signer keys, etc. vulnerable to be stolen. To protect devs from leaking keys, we have added a field called `secret` in the `Request` object. It allows you to store secrets in a vault for your AI Agent to access.

To add your secrets,

1. Edit the [default.json](https://github.com/Phala-Network/ai-agent-template-func-calling/blob/main/secrets/default.json) file or create a new JSON file in the `./secrets` folder and add your secrets to it.

```
{
  "openaiApiKey": "YOUR_OPENAI_API_KEY"
}
```

2. Run command to set the secrets

```
npm run set-secrets
# or if you have a custom JSON file
npm run set-secrets <path-to-json-file>
```

Expected output:

```sh
Use default secrets...
Storing secrets...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   205    0    68  100   137    105    213 --:--:-- --:--:-- --:--:--   319
{"token":"37a0f3f344a3bbf7","key":"343e2a7dc130fedf","succeed":true}

Secrets set successfully. Go to the URL below to interact with your agent:
https://wapo-testnet.phala.network/ipfs/QmYzBTdQNPewdhD9GdBJ9TdV7LVhrh9YVRiV8aBup7qZGu?key=343e2a7dc130fedf
Log entry added to secrets.log
```

> Note that all your secrets will be logged in file [`./logs/secrets.log`](https://github.com/Phala-Network/ai-agent-template-func-calling/blob/main/logs/secrets.log). This file is updated every time you add new secrets to your Agent Contract. If you have not published an Agent Contract, yet, this command will fail since there is not a CID to map the secrets to.
>
> Here is an example:
>
> ```
> 2024-08-29T20:30:35.480Z, CID: [QmYzBTdQNPewdhD9GdBJ9TdV7LVhrh9YVRiV8aBup7qZGu], Token: [37a0f3f344a3bbf7], Key: [343e2a7dc130fedf], URL: [https://wapo-testnet.phala.network/ipfs/QmYzBTdQNPewdhD9GdBJ9TdV7LVhrh9YVRiV8aBup7qZGu?key=343e2a7dc130fedf]
> ```

The API returns a `token` and a `key`. The `key` is the id of your secret. It can be used to specify which secret you are going to pass to your frame. The `token` can be used by the developer to access the raw secret. You should never leak the `token`.

To verify the secret, run the following command where `key` and `token` are replaced with the values from adding your `secret` to the vault.

```
curl https://wapo-testnet.phala.network/vaults/<key>/<token>
```

Expected output:

```
{"data":{"openaiApiKey":"<OPENAI_API_KEY>"},"succeed":true}
```

### Access Queries

To help create custom logic, we have an array variable named `queries` that can be accessed in the `Request` class. To access the `queries` array variable `chatQuery` value at index `0`, the syntax will look as follows:

```
const query = req.queries.chatQuery[0] as string;
```

Here is an example of adding a URL query named `chatQuery` with a value of `When did humans land on the moon`. `queries` can have any field name, so `chatQuery` is just an example of a field name and not a mandatory name, but remember to update your `index.ts` file logic to use your expected field name.

> [https://wapo-testnet.phala.network/ipfs/Qmc7EDq1X8rfYGGfHyXZ6xsmcSUWQcqsDoeRMfmvFujih3?key=51f265212c26086c&<mark style="background-color:yellow;">**chatQuery**</mark>=When%20did%20humans%20land%20on%20the%20moon](https://wapo-testnet.phala.network/ipfs/Qmc7EDq1X8rfYGGfHyXZ6xsmcSUWQcqsDoeRMfmvFujih3?key=51f265212c26086c\&chatQuery=When%20did%20humans%20land%20on%20the%20moon)

### Query Your Deployed Agent

Now that your agent is deployed, you can access the agent through a `curl` request or insert the url with the `key` and `chatQuery` defined. Here is an example of the code from the tutorial we just walked through.

Example: [https://wapo-testnet.phala.network/ipfs/QmQZYAkEz8RnX9phpWscDLsv1u7uBATaAYHb1prpFGvD4n?key=5150856fe20eb558&<mark style="background-color:yellow;">chatQuery</mark>=What%20are%20activities%20to%20do%20in%20Singapore%20today](https://wapo-testnet.phala.network/ipfs/QmQZYAkEz8RnX9phpWscDLsv1u7uBATaAYHb1prpFGvD4n?key=5150856fe20eb558\&chatQuery=What%20are%20activities%20to%20do%20in%20Singapore%20today)

### Debugging Your Agent

To debug your agent, you can use the following command:

```
curl https://wapo-testnet.phala.network/logs/all/ipfs/<CID>
```

After executing this command then you should see some output in the terminal to show the logs of requests to your agent.

```
2024-09-04T03:18:34.758Z [95f5ec53-3d71-4bb5-bbb6-66065211102c] [REPORT] END Request: Duration: 166ms
2024-09-04T03:18:34.758Z [95f5ec53-3d71-4bb5-bbb6-66065211102c] [INFO] 'Is signature valid? ' true
2024-09-04T03:18:34.758Z [95f5ec53-3d71-4bb5-bbb6-66065211102c] [INFO] 'Verifying Signature with PublicKey ' '0xC1BF8dB4D06416c43Aca3deB289CF7CC0aAFF540'
2024-09-04T03:18:34.758Z [95f5ec53-3d71-4bb5-bbb6-66065211102c] [REPORT] START Request: GET /ipfs/QmfLpQjxAMsppUX9og7xpmfSKZAZ8zuWJV5g42DmpASSWz?key=0e26a64a1e805bfd&type=verify&data=tintinland%20message%20to%20sign&signature=0x34c4d8c83406e7a292ecc940d60b34c9b11024db10a8872c753b9711cd6dbc8f746da8be9bc2ae0898ebf8f49f48c2ff4ba2a851143c3e4b371647eed32f707b1b
2024-09-04T03:17:15.238Z [768b6fda-f9f1-463f-86bd-a948e002bf80] [REPORT] END Request: Duration: 183ms
2024-09-04T03:17:15.238Z [768b6fda-f9f1-463f-86bd-a948e002bf80] [INFO] 'Signature: 0x34c4d8c83406e7a292ecc940d60b34c9b11024db10a8872c753b9711cd6dbc8f746da8be9bc2ae0898ebf8f49f48c2ff4ba2a851143c3e4b371647eed32f707b1b'
2024-09-04T03:17:15.238Z [768b6fda-f9f1-463f-86bd-a948e002bf80] [INFO] 'Signing data [tintinland message to sign] with Account [0xC1BF8dB4D06416c43Aca3deB289CF7CC0aAFF540]'
2024-09-04T03:17:15.238Z [768b6fda-f9f1-463f-86bd-a948e002bf80] [REPORT] START Request: GET /ipfs/QmfLpQjxAMsppUX9og7xpmfSKZAZ8zuWJV5g42DmpASSWz?key=0e26a64a1e805bfd&type=sign&data=tintinland%20message%20to%20sign
2024-09-04T03:16:38.507Z [3717d307-bff0-4fc0-bc98-8f66c33dd46f] [REPORT] END Request: Duration: 169ms
2024-09-04T03:16:38.507Z [3717d307-bff0-4fc0-bc98-8f66c33dd46f] [REPORT] START Request: GET /ipfs/QmfLpQjxAMsppUX9og7xpmfSKZAZ8zuWJV5g42DmpASSWz?key=0e26a64a1e805bfd
2024-09-04T03:15:00.375Z [793f58f9-f24f-4580-8ebc-04debb7d727f] [REPORT] END Request: Duration: 158ms
2024-09-04T03:15:00.375Z [793f58f9-f24f-4580-8ebc-04debb7d727f] [REPORT] START Request: GET /ipfs/QmfLpQjxAMsppUX9og7xpmfSKZAZ8zuWJV5g42DmpASSWz?key=0e26a64
a1e805bfd
```

To create logs in your Agent Contract, you can use the following syntax in your `index.ts` file.

```
// info logs
console.log('info log message!')
// error logs
console.error('error log message!')
```

For more information check the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/API/console) on `console` object.
