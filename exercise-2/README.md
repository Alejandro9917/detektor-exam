## Execise 2

### Commands
```bash
mkdir exercise-2
cd exercise-2
touch exercise-2.yaml
touch README.md
```

## Create image from exercise 1 (local)
```bash
docker build -t alejandro9917/image-exercise-1 ../exercise-1/
```

## Push image exercise 1 (local)
```bash
docker push alejandro9917/image-exercise-1
```

### Create Deployment
```bash
kubectl apply -f exercise-2.yaml
```

### Get Deployments
```bash
kubectl get pods
```

### Get Service
```bash
kubectl get services
```

### Open Minikube Tunel in other terminal
```bash
minikube tunel
```

### Testing GET Route
```bash
curl --location 'http://10.97.125.25:80/'
```