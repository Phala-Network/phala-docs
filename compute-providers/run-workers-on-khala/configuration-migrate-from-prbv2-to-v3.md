# Configuration migrate from PRBv2 to v3

This guide will show you how to migrate a PRBv2 deployment to PRBv3 using Docker Compose.

### Deploy PRBv3

First, we should create a clean PRBv3 deployment by referring to this page: [PRBv3 Deployment Guide](../run-workers-on-phala/prbv3-deployment.md)&#x20;

Make sure it's running and the `wm` should be running and listening on port 3001 by default.

### Update PRBv2 docker image

Check your `.yml` file of PRBv2 and set the docker image of `lifecycle` component to `phalanetwork/prb:git-current-v2` to receive the bundled migration script.

In the `lifecycle` , the component’s docker-compose configuration file should be like:

```yaml
lifecycle:
    network_mode: host
    image: phalanetwork/prb:git-current-v2
		# leave other things as is
```

Then run `sudo docker compose pull`.

Your will see the `lifecycle should pull a new image and restart.`

### Run the migration script

In the docker-compose folder of PRBv2's `lifecycle` component, run:

```bash
docker compose down
# Change PRB3_API_ENDPOINT to your actual endpoint of prb3-wm
docker compose run -e "PRB3_API_ENDPOINT=http://127.0.0.1:3001" --entrypoint "yarn migrate_to_prb3" lifecycle
```

To stop the PRBv2 and to run the migration script.

> There you should use the same endpoint of what you wrote in wm.yml to replace the \`http://127.0.0.1:3001\`.

Now the migration is done, click `Restart All`  button on the Worker Status page of the monitor, then wait for 15 seconds for the worker's beginning to start.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

### Limitations of Migration

#### Duplicated worker name

Before Migration, you must ensure that there can be no duplicate items in the names of the pools and workers. Includes but is not limited to worker names being equal to pool names.

#### PID #0 error

PRBv2 does not support PID #0, but PRBv3 supports it.&#x20;

This makes the migration fail if you want to migrate PID #0 from PRBv2 to PRBv3.

#### Database conflicts

If your PRBv3 is running and migration from PRBv2 is also necessary. Before your migration, check it to avoid the 2 limitations above.&#x20;

If your PRBv3 is brand new but may have some test data or you failed to migrate before, the previous test data or half-imported dirty data will result in poor synchronization results. Therefore, you need to:

* First, stop PRBv3 by `sudo docker compose down`
* Delete the `inv` and `po` folders.
* Start the normal synchronization process from the start of this article.
