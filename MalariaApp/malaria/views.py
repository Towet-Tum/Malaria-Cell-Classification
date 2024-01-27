from django.shortcuts import render, redirect
from MalariaClassifier.pipeline.predictions import PredictionPipeline, TrainModel
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
media = 'media'
import os 




# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES['upload']:
        f = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(f.name,f)
        file_url = fss.url(file)
        pred_img = os.path.join(media, file)
        pred = PredictionPipeline(pred_img)
        result = pred.makePrediction()

        context = {
            'file_url':file_url,
            'result':result,
            'pred_img':pred_img

        }
        return render(request, 'index.html', context)
        
    return render(request, 'index.html')

def train_model(request):
    os.chdir('../')
    os.system("dvc repro")

    # Get the current working directory
    current_directory = os.getcwd()
    print(f"Current Working Directory: {current_directory}")

    # Move to the next folder (replace 'next_folder' with the actual folder name)
    next_folder = 'MalariaApp'
    next_folder_path = os.path.join(current_directory, next_folder)

    # Change the current working directory to the next folder
    os.chdir(next_folder_path)

    # Print the new working directory
    new_directory = os.getcwd()
    print(f"New Working Directory: {new_directory}")
    return JsonResponse("Training completed succefully", safe=False)