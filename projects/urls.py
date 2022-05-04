from django.urls import path
from projects import views

urlpatterns = [
    path('create/', views.hello_world, name='hello_world'),
    path('get/', views.get_Project ),
    path('filter/', views.filter_projects),
]