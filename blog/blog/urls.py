from django.urls import include, path
from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls

from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),

    # Topic
    path('topics/', views.TopicList.as_view(), name='topic-list'),
    path('topics/<int:pk>/', views.TopicDetail.as_view(), name='topic-detail'),

    # Post
    path('posts/', views.PostsList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostsDetail.as_view(), name='post-detail'),
] + debug_toolbar_urls()
