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

## Build image
```bash
docker build -t image-exercise-1 .
```

## Run image
```bash
docker run -d -p 5000:5000 --name container-exercise-1 image-exercise-1
```