# PRBv3 Deployment

## Basic Requirements

To use PRBv3 (Runtime Bridge) for worker deployment, you need at least 1 additional device as the management server. The device connection is shown in the following diagram:

<figure><img src="https://github.com/doyleguo/phala-wiki-next/assets/110812052/5ccdd9d5-a4da-434b-b231-fd8e64800873" alt=""><figcaption></figcaption></figure>

> The node service and PRB service can be run on the same server as needed (depending on the number of workers and server performance).

### Server Configuration Requirements

The PRB management server needs to run 2 main components, Node and PRB. The requirements for each component are as follows:

| Components  | RAM Space | Harddisk Space | Remark                                                         |
| ----------- | --------- | -------------- | -------------------------------------------------------------- |
| Node        | 4GB+      | 900GB+ NVME    | harddisk requirement increasing, 2TB will be best              |
| PRB         | 4GB+      | 0              | RAM requirement depends on worker number, 16GB+ will be better |
| **Totally** | 32GB+     | 2TB            | -                                                              |

> You also need to ensure good network connectivity between the management server and PRB workers, and the network of the PRB management server needs to have more than 10TB of traffic space per month.

### PRB Worker requirements

PRB’s worker only needs to run a pRuntime, so the requirements for running a PRB worker are:

* Support for SGX features
* Ubuntu 22.04.2 LTS operating system and a system kernel of 5.13 or higher
* At least 4 CPU cores
* 8GB of memory
* 128GB NVME

## PRB Components Deployment

### Preparations

After installing the Ubuntu OS, first install the necessary Docker program.

```undefined
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
sudo apt install docker-compose
```

Then create a folder locally, and create a docker-compose document and other necessary documents within it.

```bash
mkdir prb-deployment
cd ./prb-deployment
touch docker-compose.yml
touch wm.yml
mkdir prb-wm-data
cd ./prb-wm-data
touch ds.yml
cd ..
```

The relationship of the file path is like：

* prb-deployment folder
  * docker-compose.yml
  * wm.yml
  * prb-wm-data folder
    * ds.yml

### Document Editing

You need to edit a total of 3 documents: the main PRB docker-compose.yml file; the wm.yml file (worker manager); and the ds.yml file (data source).

First is the main PRB docker-compose file. In this document, the following code has been added to the configuration of the node-related components. If you don’t need to run the node service and the PRB service on the same server, you can optionally delete the unnecessary parts.

Use the following command to edit the docker-compose.yml document.

```bash
vim ./docker-compose.yml 
```

After entering, you will access the document.

At this point, enter `a` and you will start editing the document. Paste the following content into the document. (Please note that the file content remains consistent and the indentation alignment of each line is consistent with this document)

```yaml
version: "3"
services:
  node:
    image: phalanetwork/phala-node-with-launcher:latest
    container_name: node
    hostname: node
    restart: always
    ports:
     - "9944:9944"
     - "9945:9945"
     - "30333:30333"
     - "30334:30334"
    environment:
     - NODE_NAME=PNODE
     - NODE_ROLE=MINER
     - PARACHAIN_EXTRA_ARGS=--max-runtime-instances 32 --runtime-cache-size 8 --rpc-max-response-size 256
     - RELAYCHAIN_EXTRA_ARGS=--max-runtime-instances 32 --runtime-cache-size 8 --rpc-max-response-size 256
    volumes:
     - /var/phala/node-data:/root/data

  wm:
    image: phalanetwork/prb3:25031701
    hostname: prb-local
    restart: always
    network_mode: host
    logging:
      options:
        max-size: "1g"
    environment:
      - MGMT_LISTEN_ADDRESSES=0.0.0.0:3001
      - RUST_BACKTRACE=1
      - RUST_LOG=info,pherry=off,phactory_api=off,prb=info
    volumes:
      - ./prb-wm-data:/var/data/prb-wm
  
  monitor:
    image: phalanetwork/prb3-monitor:latest
    restart: always
    network_mode: host
    volumes:
      - ./wm.yml:/app/public/wm.yml
```

After entering, complete the following steps to finish the text editing and save successfully.

```javascript
1、Click "esc"
2、Enter ":wq"
3、Click "Enter"，quit the editing page
```

Next is the wm.yml file. Edit the wm.yml document with the following command:

```bash
vim ./wm.yml 
```

Similarly, enter `a` to start editing the document and paste the following content into the document.

```yaml
- name: local-prb
  endpoint: http://127.0.0.1:3001
  proxied: true
```

After entering the content, save and return to the previous directory.

```javascript
1、Click "esc"
2、Enter ":wq"
3、Click "Enter"，quit the editing page
```

Finally, edit the ds document.

```bash
vim ./prb-wm-data/ds.yml 
```

enter `a` to start editing the document and paste the following content into the document.

<pre class="language-yaml"><code class="lang-yaml"><strong>---
</strong>relaychain:
  select_policy: Failover # or Random
  data_sources:
    - !SubstrateWebSocketSource
      endpoint: ws://{node-ip}:9945
      pruned: false
parachain:
  select_policy: Failover
  data_sources:
    - !SubstrateWebSocketSource
      endpoint: ws://{node-ip}:9944
      pruned: false
</code></pre>

> There are 2 parameters here that need to be user-defined: ws://{node-ip}:9945 & ws://{node-ip}:9944;
>
> You need to replace {node-ip} with the IP of the server where the node is located. If you are running the node and PRB on the same server, use your own ip there.
>
> If you don't need the PRBv3 connect to the headers-cache, delete 2 parts of&#x20;
>
> `- !HeadersCacheHttpSource`&#x20;
>
> `endpoint: http://`{headerscache-ip}`:21111`

After entering the content, save and return to the previous directory.

```javascript
1、Click "esc"
2、Enter ":wq"
3、Click "Enter", quit the editing page
```

### Program Execution

Inside the newly created folder `prb-deployment`, run the docker-compose, and the essential components for PRB will run successfully.

```undefined
sudo docker-compose up -d
```
