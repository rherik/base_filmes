from django.urls import path
from filme import views

app_name = 'filme'
urlpatterns = [
    path('', views.index, name='index'),
]
