from django.urls import path
from . import views

app_name = 'weather_app'  # Добавлено app_name


urlpatterns = [
    path('', views.index, name='index'),  #the path for our index view
]
