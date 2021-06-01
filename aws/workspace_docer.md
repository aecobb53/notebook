# AWS WorkSpaces Docker

## Installing

```bash
sudo yum install -y docker
 
sudo service docker start
 
sudo docker --version

# Docker installed under root, now to update the user

sudo groupadd docker
 
sudo usermod -aG docker $USER
 
newgrp docker 

docker --version
 
docker run hello-world

# Installing docker-compose

sudo curl -L "https://github.com/docker/compose/releases/download/1.26.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 
sudo chmod +x /usr/local/bin/docker-compose
  
$ docker-compose --version
```



