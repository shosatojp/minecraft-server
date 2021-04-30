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

### 1. Edit `docker-compose.yml` to specify **VERSION** (and memory usage).

Available versions can be found in [versions.txt](./versions.txt)

Example: `1.16.3` , `forge-1.16.3`

### (Optional) Copy mods into `mods` directory

```sh
mkdir -p server/mods
```

### 2. Agree EULA

```sh
mkdir -p server
echo 'eula=true' > server/eula.txt
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

## Backup world data with Git

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
```