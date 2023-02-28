from . import views
from django.urls import path 


urlpatterns = [
    path('welcome/',views.display)
    
]
