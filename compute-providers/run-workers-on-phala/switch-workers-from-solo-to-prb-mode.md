# Switch Workers from Solo to PRB Mode

Solo workers need to run node, pherry, and pRuntime simultaneously. If you want to switch your worker to PRB mode, you need to perform three steps:

1. Set up at least one PRB Server, details: [PRB deployment](https://docs.phala.network/compute-providers/run-workers-on-phala/prbv3-deployment)
2. Disable the Node and pherry in the Solo miner, leaving only pRuntime running
3. Add the Worker to the PRB UI, details: [Using PRBv3](https://docs.phala.network/compute-providers/run-workers-on-phala/using-prbv3-ui)

If you are using the docker compose content under this Wiki: [Solo worker deployment](https://docs.phala.network/compute-providers/run-workers-on-phala/solo-worker-deployment)

The command to disable Node and pherry is as follows:

```bash
sudo docker container rm -f node
sudo docker container rm -f phala-pherry
```

> If you have customized the docker compose content, please use `sudo docker container ps` to query the running service names and replace `node` and `phala-pherry` in the above commands.
