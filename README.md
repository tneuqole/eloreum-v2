eloreum-v2

```
sudo yum install docker
sudo gpasswd -a ec2-user docker
sudo systemctl start docker

docker run -d --restart unless-stopped \
    -v $HOME/minecraft-server:/data \
    -p 25565:25565 \
    -e TYPE=FABRIC -e EULA=TRUE -e MEMORY=3G \
    --name mc itzg/minecraft-server:java16
    
docker run -d --restart unless-stopped \
 -p 7777:7777 \
 -v $HOME/terraria:/root/.local/share/Terraria/Worlds \
 --name terraria ryshe/terraria:latest \
 -world /root/.local/share/Terraria/Worlds/eloreum.wld \
 -autocreate 3
```
