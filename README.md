# Dockerized Minecraft Server

* vanilla or forge server

## Create Working Directory

```sh
# copy files and discard git directory
git clone https://github.com/shosatojp/minecraft-server ./my-server
cd ./my-server
rm -rf .git .gitignore
```

## Build Server (Vanilla)

### 1. Edit `docker-compose.yml` to specify **VERSION** (and memory usage).

Available versions can found in [versions.txt](./versions.txt)

Example: `1.12.2`

### 2. Make world directory

```sh
mkdir -p world
# if you forgot this step, run `sudo chown -R $UID:$GID world`
```

### 3. Confirm EULA

```sh
echo 'eula=true' > eula.txt
```

### 4. Start Server

```sh
sudo docker-compose up --build -d
```

### (Optional) Edit `server.properties`

```sh
# edit and restart
sudo docker-compose restart
```

## Build Server (Forge)

### 1. Edit `docker-compose.yml` to specify **version** (and memory usage).

Available versions can found in [versions.txt](./versions.txt)

Example: 
`forge-1.12.2`

### 2. Make `world` and `mods` directory

```sh
mkdir -p world mods
# if you forgot this step, run `sudo chown -R $UID:$GID world mods`
```


### 3. Copy mods into `mods` directory

### 4. Confirm EULA

```sh
echo 'eula=true' > eula.txt
```

### 5. Start Server

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

```sh
# create repository `yourname/my-server`
git init
git remote add origin https://github.com/yourname/my-server
echo -e '/logs/\n/crash-reports/' >> '.gitignore'
git add .
git commit -m 'create server'
git push --set-upstream master origin
```