# Access Database

Phala Cloud supports running a database locally or connecting to an external database. There is no difference in how you access a database compared to a general server. To save your data to disk, **you need to** [**configure volumes**](https://docs.docker.com/reference/compose-file/volumes/) **in the Docker Compose file** and write data to the correct path, here is an example from Docker website.

```yaml
services:
  backend:
    image: example/database
    volumes:
      - db-data:/etc/data

  backup:
    image: backup-service
    volumes:
      - db-data:/var/lib/backup/data

volumes:
  db-data:
```
