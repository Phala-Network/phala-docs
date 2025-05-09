# Configure a Private Log Viewer

## Securing Your Docker Logs

For enhanced security, you may want to restrict log access to specific individuals. You can configure a private log viewer in your Docker Compose file using open-source tools like [Dozzle](https://github.com/amir20/dozzle).

### Implementation Steps

1. **Generate Authentication Credentials**

   On your local machine, generate a Dozzle user authority token using the following command:
   
   ```bash
   docker run amir20/dozzle generate --name Admin --email me@email.net --password secret admin | base64 -w 1000
   ```
   
   This example creates a user with:
   - Username: "Admin"
   - Password: "secret"
   - Role: "admin"

2. **Configure Dozzle in Docker Compose**

   Add the following services to your Docker Compose file:
   
   ```yaml
   services:
     # Setup service to initialize user data
     setup:
       image: busybox
       restart: "no"
       volumes:
         - dozzle-data:/dozzle-data/
       command: >
         sh -c 'echo "use authority token" | base64 -d > /dozzle-data/users.yml || true'
   
     # Dozzle log viewer service
     dozzle:
       container_name: dozzle
       image: amir20/dozzle:latest
       depends_on:
         - setup
       environment:
         - DOZZLE_AUTH_PROVIDER=simple
       volumes:
         - /var/run/docker.sock:/var/run/docker.sock
         - dozzle-data:/data/
       ports:
         - 8080:8080
   ```

3. **Access Protected Logs**

   Once deployed, you can access the logs through the container's public endpoint using the credentials you configured. Only authorized users with the correct username and password will be able to view the logs.
