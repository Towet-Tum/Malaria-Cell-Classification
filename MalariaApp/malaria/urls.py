from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('train_model/', views.train_model, name='train_model')
]