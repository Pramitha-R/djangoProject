from . import views
from django.urls import path 


urlpatterns = [
    
    path('ui/', views.index)
]
