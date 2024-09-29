# Git init
```bash
git init
touch .gitignore
```

## Exercise 1

### Commands
```bash
mkdir exercise-1 
cd exercise-1
touch Dockerfile
touch app.py
touch requeriments.txt
```

### Build image
```bash
docker build -t image-exercise-1 .
```

### Run image
```bash
docker run -d -p 5000:5000 --name container-exercise-1 image-exercise-1
```

## Exercise 3

### Commands
```bash
mkdir exercise-3
cd exercise-3
mkdir gps
mkdir testing
mkdir utils
touch Dockerfile
touch app.py
touch requeriments.txt
touch docker-compose.yaml
touch init.sql
touch gps/service.py
touch utils/db.py
touch utils/json.py
touch test.sql
```

### Build image
```bash
docker build -t image-exercise-3 .
```

### Run image
```bash
docker run -d -p 5000:5000 --name container-exercise-3 image-exercise-3
```

### Run Docker Compose
```bash
 docker-compose up
```

### Testing Post Route
```bash
curl --location 'http://127.0.0.1:5000/v1/gps' \
--header 'Content-Type: application/json' \
--data '{
    "device_id": 1,
    "latitude": 47.7749,
    "longitude": -122.4194,
    "altitude": 30.5,
    "speed": "20",
    "timestamp": "1727566206"    
}'
```

### Testing Post Route
```bash
curl --location 'http://127.0.0.1:5000/v1/getData'
```