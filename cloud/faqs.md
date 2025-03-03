
# 📬 FAQs

1. **Can the encrypted environment variable be accessed by any other part, including the host OS?**
    
    No, it's encrypted on the client side and sent to the CVM using X25519 encryption scheme. The variables can only be decrypted inside the CVM.
    
2. **Can Docker logs be accessed by any other part, including the host OS?**
    
    Currently, the logs are not end-to-end encrypted. However, you can decide whether to make them public under **Advanced Features → Public Logs** during deployment. If you choose public, anyone with the log URL can view them, and the Log URL can be inferred from your instance ID in the public endpoints. If you choose private, no one can access the logs, and you'll need to configure a log viewer to view them elsewhere.
    
3. **Is application data persistent on the disk?**
    
    Yes, the data you write to the filesystem inside Docker will persist on the disk and be encrypted. Restarting or upgrading will not affect data recovery. To save data on disk, you need to [configure volumes](https://docs.docker.com/reference/compose-file/volumes/) in the Docker Compose file and write data to the correct path.
    
4. **How can others verify that my application is running inside a TEE?**
    
    Once the application is successfully launched, you can prove this by providing the RA Report, which can be exported through an endpoint by your Docker application. The RA Report is linked with the application's runtime information, such as the Docker image hash, the initial arguments passed to the container, and the environment variables.