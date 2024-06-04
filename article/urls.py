from django.urls import path
from .views import *

app_name = 'article'

urlpatterns = [
    path('', articles_list, name='list'),
    path('dashboard/', my_articles, name='dashboard'),
    path('detail/<int:id>', article_detail, name='detail'),
    path('create/', article_create, name='create'),
    path('update/<int:id>', article_update, name='update'),
    path('delete/<int:id>', article_delete, name='delete'),
    path('comment-create/<int:id>', comment_create, name='comment-create'),
]