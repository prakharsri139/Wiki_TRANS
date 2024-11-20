from django.urls import path 
from .views import *
  
urlpatterns = [ 
    path('', wiki_search,name="wiki_search"), 
]