
# 📕 Deployment Cheat Sheet

1. **Build docker image on x86 linux**
    
    Since some developers use Mac ARM, we highly recommend using an x86 machine to build your Docker images before deploying them to our cloud to avoid compatibility issues.
    
    See also:
    
    [Multi-platform](https://docs.docker.com/build/building/multi-platform/)
    
    [How to build x86 (and others!) Docker images on an M1 Mac](https://blog.jaimyn.dev/how-to-build-multi-architecture-docker-images-on-an-m1-mac/)
    
    [Run or build x86_64 Docker image on Apple M1, M2, and M3](https://nesin.io/blog/x86-x86-amd64-docker-mac)
    
2. **Limit the size of your docker logs to save disk usage**
    
    You can config **logging** options for all of your services to limit the size of the docker logs.
    
    ```yaml
    x-common: &common-config
      restart: always
      logging:
        driver: "json-file"
        options:
          max-size: "100m"
          max-file: "5"
    
    services:
      example:
        <<: *common-config
        image: example:0.1.0
        container_name: example
        ports:
          - "8000:8000"
    ```
