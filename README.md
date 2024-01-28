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

xQQJ99j4FWBwjFJ4qY2rv2Eiy+cLDDvW1JceqUFF8F+ACRCqt7Bc


I8I6SL/4TWji9hq2KriMZB6JMT+ugZ97BgdOp9Dpb/+ACRCj5SZv

## Azure Deployment

docker build -t malaria.azurecr.io/malaria:latest .

docker login malaria.azurecr.io

docker push malaria.azurecr.io/malaria:latest
