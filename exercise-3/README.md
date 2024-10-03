### Create folder and files
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

### Build image (local)
```bash
docker build -t image-exercise-3 .
```

### Run image (local)
```bash
docker run -d -p 3000:3000 --name container-exercise-3 image-exercise-3
```

### Run Docker Compose (local)
```bash
 docker-compose up
```

## Push image exercise
```bash
docker push alejandro9917/image-exercise-3
```

## Edit docker-compose.yaml
```bash
vi docker-compose.yaml
```

## Edit init.sql 
```bash
vi init.sql
```

### Run Docker Compose
```bash
docker compose up
```

### Testing Post Route
```bash
curl --location 'http://34.138.157.105:5000/v1/gps' \
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

### Testing GET Route
```bash
curl --location 'http://34.138.157.105:5000/v1/getData'
```

### Run Testing
```bash
python test.py
```