from django.urls import path
from projects import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]