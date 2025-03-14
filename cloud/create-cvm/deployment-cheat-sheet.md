# Deployment Cheat Sheet

## Platform Compatibility

### Build Docker Images on x86 Linux

When developing on Mac ARM (M1/M2/M3), build your Docker images on an x86 machine before cloud deployment to prevent compatibility issues.

**Resources:**

* [Docker Multi-platform Builds](https://docs.docker.com/build/building/multi-platform/)
* [Building x86 Docker Images on M1 Macs](https://blog.jaimyn.dev/how-to-build-multi-architecture-docker-images-on-an-m1-mac/)
* [Running x86\_64 Docker Images on Apple Silicon](https://nesin.io/blog/x86-x86-amd64-docker-mac)

## Performance Optimization

### Limit Docker Log Size

Configure logging options for all services to prevent excessive disk usage:

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
