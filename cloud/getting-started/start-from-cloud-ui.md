# Your First CVM Deployment

{% hint style="warning" %}
Make sure you have gone through the [Sign-up for Cloud Account](sign-up-for-cloud-account.md) section before continuing.
{% endhint %}

## Step 1 - Create a CVM

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption><p>Create CVM</p></figcaption></figure>

Click the **Deploy** -> **docker-compose.yml** in the top-right corner of the cloud [dashboard](https://cloud.phala.network/dashboard). Once there, you need to:

1. Set your application name (e.g. "hello-world")
2.  Paste the config file to describe your service in docker compose format. In this tutorial, we deploy a basic jupyter-notebook without any code change.

    <figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption><p>Docker Compose File</p></figcaption></figure>

    ```yaml
    services:
      jupyter:
        image: quay.io/jupyter/base-notebook
        ports:
          - 8080:8888
        volumes:
          - /var/run/tappd.sock:/var/run/tappd.sock
        environment:
          - GRANT_SUDO=yes
        user: root
        command: "start-notebook.sh --NotebookApp.token=${TOKEN}"
    ```
3.  Choose the resource plan. There are some preset plans available, or you can customize them for more flexibility. In **Node & Image** section, we recommend choosing **dstack-dev-** as guest image if you are deploying for testing. It will enable the debug feature that you can login to the virtual machine in the future.\


    <figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption><p>Compute Resources</p></figcaption></figure>
4.  (Optional) Set **Encrypted Secrets**. Encrypted Secrets are variables that can be referenced in your docker compose file. It's end-to-end encrypted between you and the app you deployed. In this guide, we set the environment variable **`TOKEN`** to **`phala`** for testing. Later you will use this token to login to the notebook. Note that `TOKEN` is referenced in the `command` field in the compose file.\
    &#x20; &#x20;

    <figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption><p>Encrypted Secrets</p></figcaption></figure>
5.  Click the **Deploy** button to start the deployment process. You will need to wait for a few minutes as the cloud sets everything up. In the meantime, you can enter the CVM details page by clicking the CVM card, and choose **Logs** > **serial** to view the OS log outputs. Note this is the logs of CVM, not your application logs.\


    <div align="center" data-full-width="false"><figure><img src="../../.gitbook/assets/image (4).png" alt="" width="375"><figcaption><p>The CVM is starting</p></figcaption></figure></div>

    <figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption><p>View CVM serial logs</p></figcaption></figure>
6.  After the deployment is complete, navigate through **CVM Details → Network** to see the public endpoint of your application.\


    <figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption><p>App Endpoints</p></figcaption></figure>
7. You can use these endpoints to access the application if you have service serve on. You will find the endpoint is composed of **App ID** and **Port**. In this example:
   * Endpoint: `https://1e598a2f983dd80c413627e0b50d91905f3f48be-8080.dstack-prod2.phala.network`&#x20;
   * It contains the following components:
     * `App ID`: `1e598a2f983dd80c413627e0b50d91905f3f48be`
     * `Port`: `8080`
     * `Gateway Domain`: `dstack-prod2.phala.network`
   * The reason why we have a port number **8080** here is that the default port of jupyter notebook is 8888, but we configure the port mapping to 8080 in the docker compose file. You can check the docker compose file in **Compose File** tab and you will find **8080:8888** in the Compose File content.
8.  Access the endpoint. You will see the jupyter notebook interface. Type the token you set in the previous step and you will be able to access the jupyter notebook.

    <figure><img src="../../.gitbook/assets/cloud-jupyter-notebook.png" alt="jupyter-notebook"><figcaption><p>Access your app</p></figcaption></figure>
9.  View the logs of your application. You can switch to **Containers** tab and click **View Logs** to view container logs.&#x20;

    <figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

For example, the logs of the container **jupyter** are as follows:

```
2025-03-04T03:18:05.828657314Z Entered start.sh with args: start-notebook.sh --NotebookApp.token=*****
2025-03-04T03:18:05.842663875Z Running hooks in: /usr/local/bin/start-notebook.d as uid: 0 gid: 0
2025-03-04T03:18:05.842682502Z Done running hooks in: /usr/local/bin/start-notebook.d
2025-03-04T03:18:05.856699933Z Granting jovyan passwordless sudo rights!
2025-03-04T03:18:05.864340938Z Running hooks in: /usr/local/bin/before-notebook.d as uid: 0 gid: 0
2025-03-04T03:18:05.864358165Z Sourcing shell script: /usr/local/bin/before-notebook.d/10activate-conda-env.sh
2025-03-04T03:18:06.527587460Z Done running hooks in: /usr/local/bin/before-notebook.d
2025-03-04T03:18:06.527720112Z Running as jovyan: start-notebook.sh --NotebookApp.token=*****
2025-03-04T03:18:06.542227731Z WARNING: Use start-notebook.py instead
2025-03-04T03:18:07.221798177Z [I 2025-03-04 03:18:07.221 ServerApp] jupyter_lsp | extension was successfully linked.
2025-03-04T03:18:07.225295903Z [I 2025-03-04 03:18:07.225 ServerApp] jupyter_server_terminals | extension was successfully linked.
2025-03-04T03:18:07.226629073Z [W 2025-03-04 03:18:07.226 LabApp] 'token' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
2025-03-04T03:18:07.228942619Z [W 2025-03-04 03:18:07.228 ServerApp] ServerApp.token config is deprecated in 2.0. Use IdentityProvider.token.
2025-03-04T03:18:07.229062498Z [I 2025-03-04 03:18:07.229 ServerApp] jupyterlab | extension was successfully linked.
2025-03-04T03:18:07.231919391Z [I 2025-03-04 03:18:07.231 ServerApp] nbclassic | extension was successfully linked.
2025-03-04T03:18:07.235213471Z [I 2025-03-04 03:18:07.235 ServerApp] notebook | extension was successfully linked.
2025-03-04T03:18:07.236333327Z [I 2025-03-04 03:18:07.236 ServerApp] Writing Jupyter server cookie secret to /home/jovyan/.local/share/jupyter/runtime/jupyter_cookie_secret
2025-03-04T03:18:07.433001809Z [I 2025-03-04 03:18:07.432 ServerApp] notebook_shim | extension was successfully linked.
2025-03-04T03:18:07.447337226Z [W 2025-03-04 03:18:07.447 ServerApp] WARNING: The Jupyter server is listening on all IP addresses and not using encryption. This is not recommended.
2025-03-04T03:18:07.447791187Z [I 2025-03-04 03:18:07.447 ServerApp] notebook_shim | extension was successfully loaded.
2025-03-04T03:18:07.449649812Z [I 2025-03-04 03:18:07.449 ServerApp] jupyter_lsp | extension was successfully loaded.
2025-03-04T03:18:07.450667373Z [I 2025-03-04 03:18:07.450 ServerApp] jupyter_server_terminals | extension was successfully loaded.
2025-03-04T03:18:07.451876678Z [I 2025-03-04 03:18:07.451 LabApp] JupyterLab extension loaded from /opt/conda/lib/python3.12/site-packages/jupyterlab
2025-03-04T03:18:07.451953256Z [I 2025-03-04 03:18:07.451 LabApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
2025-03-04T03:18:07.452411500Z [I 2025-03-04 03:18:07.452 LabApp] Extension Manager is 'pypi'.
2025-03-04T03:18:07.491767074Z [I 2025-03-04 03:18:07.491 ServerApp] jupyterlab | extension was successfully loaded.
2025-03-04T03:18:07.494788105Z [I 2025-03-04 03:18:07.494 ServerApp] nbclassic | extension was successfully loaded.
2025-03-04T03:18:07.497626731Z [I 2025-03-04 03:18:07.497 ServerApp] notebook | extension was successfully loaded.
2025-03-04T03:18:07.499274664Z [I 2025-03-04 03:18:07.499 ServerApp] Serving notebooks from local directory: /home/jovyan
2025-03-04T03:18:07.499368871Z [I 2025-03-04 03:18:07.499 ServerApp] Jupyter Server 2.15.0 is running at:
2025-03-04T03:18:07.499442171Z [I 2025-03-04 03:18:07.499 ServerApp] http://localhost:8888/lab?token=...
2025-03-04T03:18:07.499491353Z [I 2025-03-04 03:18:07.499 ServerApp]     http://127.0.0.1:8888/lab?token=...
2025-03-04T03:18:07.499530802Z [I 2025-03-04 03:18:07.499 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
2025-03-04T03:18:07.517241317Z [I 2025-03-04 03:18:07.517 ServerApp] Skipped non-installed server(s): bash-language-server, dockerfile-language-server-nodejs, javascript-typescript-langserver, jedi-language-server, julia-language-server, pyright, python-language-server, python-lsp-server, r-languageserver, sql-language-server, texlab, typescript-language-server, unified-language-server, vscode-css-languageserver-bin, vscode-html-languageserver-bin, vscode-json-languageserver-bin, yaml-language-server
```

## Step2 - Verify TEE Proof

1.  Check the default RA Report. We provide a default [Remote Attestation Report](https://sgx101.gitbook.io/sgx101/sgx-bootstrap/attestation#remote-attestation-primitives) (also known as TEE Proof), which is displayed in the CVM detailed page. To view the entire report, click **View Details → Attestations**.\


    <figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption><p>Attestations</p></figcaption></figure>
2.  By clicking the **Check Attestation** button in the certificate chain section, you will be redirected to the [TEE Proof Explorer](https://proof.t16z.com/), where you can verify the quote. You can share this quote with anyone, as it serves as proof that your program is running inside a genuine TEE.\


    <figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption><p>Check Attestation</p></figcaption></figure>

    You can also request customized Remote Attestation reports programmably via API here: [generate-ra-report.md](../../phala-cloud/phala-cloud-user-guides/building-with-tee/generate-ra-report.md "mention").

## Next Steps

Now that you've deployed your first confidential application, you can:

1. **Deploy your existing Docker applications** to TEE - check out the [Deploy Docker App in TEE](../../migration.md)
2. **Build an AI agent** in minutes and deploy in one-click with the [Eliza Agent Builder](https://cloud.phala.network/eliza) - check out the [tutorial](https://phala.network/posts/guide-to-exploring-the-phala-cloud-agent-builder) to get started
3. **Explore advanced features** like debugging, log management, and scaling your applications
