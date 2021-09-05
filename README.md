# Dockerized Minecraft Server

* vanilla or forge server
* 1.2.1 - 1.17.1


## Build Server

### 0. Prerequirements

- Docker
- docker-compose

### 1. Create Working Directory

```sh
# copy files and discard git directory
git clone https://github.com/shosatojp/minecraft-server ./my-server
cd ./my-server
rm -rf .git .gitignore
```

### 2. Edit `docker-compose.yml` to specify **VERSION** and agree to **eula**

Available versions can be found in [versions.json](./versions.json)

Example: 
```yml
VERSION: "1.17.1"
VERSION: "forge-1.12.2"
```

```yml
eula: "true"
```

change owner to runtime user & group as you like.

```yml
user: "nobody:nogroup"
```

### 3. Make server directory

server directory must be runtime user & group.

```sh
mkdir -p server
sudo chown -R nobody:nogroup server
```

### (Optional) Copy mods into `mods` directory

```sh
mkdir -p server/mods
sudo chown -R nobody:nogroup server
```

### 4. Start Server

```sh
sudo docker-compose up --build -d

# check logs
sudo docker-compose logs -f
```

### (Optional) Edit `server.properties`

```sh
# edit and restart
sudo docker-compose restart
```

### (Optional) Start or stop server

```sh
sudo docker-compose stop
sudo docker-compose start
sudo docker-compose restart
```

## Manage server

```sh
# find your container name
$ sudo docker-compose ps
#             Name                        Command            State            Ports          
# -------------------------------------------------------------------------------------------
# minecraft-server_minecraft_1   /bin/sh -c /data/start.sh   Up      0.0.0.0:25565->25565/tcp

`minecraft-server_minecraft_1` is your container name


# attach to container
$ sudo docker attach minecraft-server_minecraft_1


# now you can use minecraft commands
whitelist add hoge
```



## Trouble shootings

### `cannot create directory 'world': Permission denied`

confirm owner of the `server` directory is run time user and group

```sh
sudo chown -R nobody:nogroup server/
```

### `You need to agree to the EULA in order to run the server.`

check your `docker-compose.yml` and confirm that `eula: "true"`.

<!-- ## Backup world data with Git

* backup

```sh
# create repository `yourname/my-server`
git init
git remote add origin https://github.com/yourname/my-server
echo -e '/server/logs/\n/server/crash-reports/' >> '.gitignore'
git add .
git commit -m 'create server'
git push --set-upstream master origin
```

* restore

```sh
git clone https://github.com/yourname/my-server
cd ./my-server
sudo docker-compose up --build -d
``` -->