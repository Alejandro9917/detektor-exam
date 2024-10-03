
## Execise 4

### Commands
```bash
mkdir exercise-4
cd exercise-4
touch cloudbuild.yaml
touch README.md
```

### Enable Google Cloud Build
```bash
gcloud services enable cloudbuild.googleapis.com
```

### Asign permissions
```bash
gcloud projects add-iam-policy-binding [PROJECT_ID] \
    --member=serviceAccount:[PROJECT_NUMBER]@cloudbuild.gserviceaccount.com \
    --role=roles/container.developer
```

### Create GKE
```bash
gcloud container clusters create candidato2 \
    --num-nodes=3 \
    --zone=us-uest1-b
```

### Connect kubectl to cluster
```bash
gcloud container clusters get-credentials candidato2 \
    --zone us-uest1-b
```

### Run Pipeline
```bash
gcloud builds submit --config=cloudbuild.yaml .
```