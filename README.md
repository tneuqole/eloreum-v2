eloreum-v2

```
docker run -d --restart unless-stopped \
    -v /home/ec2-user/minecraft-server:/data \
    -p 25565:25565 \
    -e TYPE=FABRIC -e EULA=TRUE -e MEMORY=3G \
    --name mc itzg/minecraft-server:java16
```
