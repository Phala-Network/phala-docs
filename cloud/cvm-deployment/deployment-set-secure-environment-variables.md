
# Set Secure Environment Variables

If your application requires environment variables, **DO NOT** **set them directly in the Docker Compose file**. Instead, set them through the **Encrypted Secrets** section.

1. First you need to declare the environments in Docker compose file like below:
    
    ```python
    services:
      your-service:
    	  environment:
    	      - OPENAI_API_KEY=${OPENAI_API_KEY_IN_ENV}
    	      - TWITTER_API_KEY=${TWITTER_API_KEY_IN_ENV}
    ```
    
    And **DO NOT** set environment with double quotation marks `OPENAI_API_KEY="${OPENAI_API_KEY_IN_ENV}"`
    
2. Then set ENV values in **Encrypted Secrets** section.

<figure><img src="../../.gitbook/assets/cloud-set-env.png" alt="set-env"><figcaption></figcaption></figure>
