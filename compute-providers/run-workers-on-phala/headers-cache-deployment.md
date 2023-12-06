# Headers-cache deployment

## What's the Header-cache

The headers-cache is a component that stores the header of each block. The block header includes important information such as previous block hash, timestamp, nonce, and so on, representing all the transactions in the block.

Caching block headers can improve efficiency when downloading and synchronizing with the network, once you are using a pherry or PRB to sync the pRuntime, add a headers-cache between them will significantly reduce the sync period.

## Headers-cache requirements

* 2GB of memory
* 200GB NVME - for Phala headers-cache; 500GB NVME for Khala headers-cache

## Steps for deployment

### Preparations

Create a folder locally, and create a docker-compose document within it.

```
mkdir headers-cache
cd ./headers-cache
touch docker-compose.yml
```

### Document Editing

Use the following command to edit the docker-compose.yml document.

```bash
vim ./docker-compose.yml 
```

Enter `a` and you will start editing the document. Paste the following content into the document. (Please note that the file content remains consistent and the indentation alignment of each line is consistent with this document)

```
version: "3"
services:
  phala-headers-cache:
    image: phalanetwork/phala-headers-cache:latest
    container_name: phala-headers-cache
    restart: always
    environment:
      - ROCKET_PORT=21111
      - ROCKET_ADDRESS=0.0.0.0
      - RUST_LOG=info
    command:
      - serve
      - --grab-headers
      - --grab-para-headers
      - --grab-storage-changes
      - --node-uri=ws://node:9945
      - --para-node-uri=ws://node:9944
      - --grab-storage-changes-batch=1
      - --token=
      - --check-batch=500000
    ports:
      - 21111:21111
    volumes:
      - /opt/headers-cache/data/cache.db
```

After entering, complete the following steps to finish the text editing and save successfully.

```javascript
1、Click "esc"
2、Enter ":wq"
3、Click "Enter"，quit the editing page
```

### Program Execution

Inside the newly created folder `headers-cache`, run the docker-compose, and the essential components for PRB will run successfully.

```
sudo docker compose up -d
```
