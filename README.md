# Malaria-Cell-Classification
This Malaria Cell Classification Using Deep Learning Technique





MLFLOW_TRACKING_URI=https://dagshub.com/Towet-Tum/Malaria-Cell-Classification.mlflow \
MLFLOW_TRACKING_USERNAME=Towet-Tum \
MLFLOW_TRACKING_PASSWORD=39c66009c3d7d6d659cbc691e65a93c46873d3c4 \
python script.py




```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Towet-Tum/Malaria-Cell-Classification.mlflow

export MLFLOW_TRACKING_USERNAME=Towet-Tum

export MLFLOW_TRACKING_PASSWORD=39c66009c3d7d6d659cbc691e65a93c46873d3c4

```

## Saved password

7cekEE9WEfjAI5sJurF3MemA+mJl1N4Sqvck9owDyy+ACRA4usR7

2iJ8Uu0cF+9shcS/SLT0tjXXIBmSaD/Egi+4N83GVQ+ACRDEmMOa

## Azure Deployment

docker build -t malaria.azurecr.io/malaria-cell-app:latest

docker login malaria.azurecr.io

docker push malaria.azurecr.io/malaria-cell-app:latest
