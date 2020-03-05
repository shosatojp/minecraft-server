```sh

sudo docker build . -t minecraft-server
sudo docker run -d -it -p=25565:25565 minecraft-server

```