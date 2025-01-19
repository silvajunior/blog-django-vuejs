from django.urls import path
from .views import PostList, PostDetail, PostCreate

urlpatterns = [
    path('api/posts/', PostList.as_view(), name='post-list'),
    path('api/posts/create/', PostCreate.as_view(), name='post-create'),
    path('api/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
