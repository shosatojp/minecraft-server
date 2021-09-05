# Dockerized Minecraft Server

* vanilla or forge server

## Create Working Directory

```sh
# copy files and discard git directory
git clone https://github.com/shosatojp/minecraft-server ./my-server
cd ./my-server
rm -rf .git .gitignore
```

## Build Server

### 1. Edit `docker-compose.yml` to specify **VERSION** and agree to **eula**

Available versions can be found in [versions.json](./versions.json)

Example: 
```
VERSION: "1.17.1"
VERSION: "forge-1.12.2"
```

```
eula: "true"
```

### 2. Make server directory

change owner to runtime user & group as you like.

```sh
mkdir -p server
sudo chown -R nobody:nogroup server
```

### (Optional) Copy mods into `mods` directory

```sh
mkdir -p server/mods
sudo chown -R nobody:nogroup server
```

### 3. Start Server

```sh
sudo docker-compose up --build -d
```

### (Optional) Edit `server.properties`

```sh
# edit and restart
sudo docker-compose restart
```

## Stop Server

```sh
sudo docker-compose stop
```

## Restart Server

```sh
sudo docker-compose start
```

## Trouble Shoot

### `cannot create directory 'world': Permission denied`

confirm owner of the `server` directory is run time user and group

```sh
sudo chown -R nobody:nogroup server/
```

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