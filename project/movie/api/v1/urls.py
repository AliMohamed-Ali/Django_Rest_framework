from django.urls import path
from .views import hello,movie_list,movie_create,movie_detail,movie_delete,movie_update

app_name = 'movie_v1'
urlpatterns = [
    path('hello-api', hello, name='hello-api'),
    path('movie_list', movie_list, name='movie-list'),
    path('movie_create', movie_create, name='movie-create'),
    path('movie/<int:pk>', movie_detail, name='movie-detail'),
    path('movie/<int:pk>/delete', movie_delete, name='movie-delete'),
    path('movie/<int:pk>/update', movie_update, name='movie-update'),
]
