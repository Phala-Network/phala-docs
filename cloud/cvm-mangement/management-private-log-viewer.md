
# Set Private Log Viewer

In most cases, you may not want anyone except specific individuals to see the logs. To make your Docker logs private, you can configure a log viewer in the Docker Compose file. For example, you can use the open-source log viewer [Dozzle](https://github.com/amir20/dozzle).

1. Generate user data
    
    On your local machine, generate a Dozzle user authority token using the Dozzle container by running the following command. In this example, we set the username as "Admin," the password as "secret," and the role as "admin.”
    
    ```python
    docker run amir20/dozzle generate --name Admin --email me@email.net --password secret admin | base64 -w 1000
    ```
    
2. Then, setup Dozzle in Docker compose file.
    
    ```python
    services:
      # Viewable logs with dozzle
      setup:
        image: busybox
        restart: "no"
        volumes:
          - dozzle-data:/dozzle-data/
        command: >
          sh -c 'echo "use authority token" | base64 -d > /dozzle-data/users.yml || true'
    
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
    
3. Once the application is running, you will only be able to view the logs using the username and password you set earlier, accessed through the relevant container's public endpoint.
