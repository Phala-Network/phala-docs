
# Deploy CVM with Template

**Step1- Deploy a CVM with Template**

Click the **Deploy** button in the top-right corner of the cloud [homepage](https://cloud.phala.network/register?invite=PHALAWIKI) to access the deployment dashboard. Once there, you need to:

1. Set your application name
2. Choose a template you want to get started or use your Docker compose file.
    
    📍 For ElizaOS/Eliza, we recommend changing the image name to **registry-cache.phala.systems/phalanetwork/eliza:v0.1.6-alpha.4** in the Compose file to use the cached image to save downloading time. **Head to the [tutorial](https://www.notion.so/Deploy-Eliza-in-Phala-Cloud-1770317e04a180ecacd2e2af97d25bb7?pvs=21) to see how to play**.

    <figure><img src="../../.gitbook/assets/cloud-deploy-new-cvm.png" alt="Deploy New CVM"><figcaption></figcaption></figure>
    
3. Choose the compute resources. There are some preset plans available, or you can customize them for more flexibility.
    1. For the template **`kennethreitz/httpbin`**, we recommend choosing **TEE Starter**.
    2. For **`elizaOS/eliza`**, we recommend choosing at least **TEE Pro**.
        
        <figure><img src="../../.gitbook/assets/cloud-config-compute-resource.png" alt="config-compute-resource"><figcaption></figcaption></figure>
        
4. Click the **Deploy** button to start the deployment process. You will need to wait for a while as the backend sets everything up.
5. After the deployment is complete, navigate through **View Details → Network** to see the endpoint information. You can use these endpoints to access the application if you have service serve on.
    
    <figure><img src="../../.gitbook/assets/cloud-cvm-details.png" alt="cvm-details"><figcaption></figcaption></figure>
    
    Or switch to **Containers** tab to view container logs. For example, **if you have deployed Eliza, you can see logs in Eliza container like below**:
    
    ```yaml
    [37m ◎ LOGS
    [37m Registering service: [0m
    [37m aws_s3 [0m
    32m ["✓ Service aws_s3 registered successfully"] [0m
    
    [37m ["◎ Room b850bc30-45f8-0041-a00a-83df46d8555d created successfully."]
    [32m ["**✓ User Eliza created successfully**."] [0m
    [32m ["✓ Service browser initialized successfully"] [0m
    Initializing ImageDescriptionService
    ```

**Step2 - Verify TEE Proof**

1. Check the default RA Report
    
    We provide a default [Remote Attestation Report](https://sgx101.gitbook.io/sgx101/sgx-bootstrap/attestation#remote-attestation-primitives) (also known as TEE proof), which is displayed in the Worker Dashboard. To view the entire report, click **View Details → Attestation**.
    
    <figure><img src="../../.gitbook/assets/cloud-attestation-page.png" alt="attestation-page"><figcaption></figcaption></figure>
    
2. By clicking the **Check Attestation** button in the certificate chain section, you will be redirected to the [quote explorer](https://proof.t16z.com/), where you can verify the quote. You can share this quote with anyone, as it serves as proof that your program is running inside a genuine TEE.

**Next Steps**

1. **Deploy an Eliza AI Agent in Minutes with the Eliza Template**
2. Create your own application by checking out **Migrate Applications to TEE.**
