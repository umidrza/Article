from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    path('', articles_list, name='list')
]