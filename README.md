
## Build Server

### 1. Edit `docker-compose.yml` to specify **version** (and memory usage).

### 2. Make world directory

```sh
mkdir -p world
# if you forgot this step, run `sudo chown -R $UID:$GID`
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

## Stop Server

```sh
sudo docker-compose stop
```

## Restart Server

```sh
sudo docker-compose start
```