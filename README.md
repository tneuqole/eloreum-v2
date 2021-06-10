eloreum-v2

```
docker run -d -v ~/minecraft-server:/data \
    -e TYPE=FABRIC \
    -p 25565:25565 -e EULA=TRUE -e MEMORY=3G \
    --name mc itzg/minecraft-server
```
