from django.urls import include, path
from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.authtoken import views as drf_auth_views


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


    path('api-auth/', include('rest_framework.urls')),
    path('users/posts/', views.UserPostsList.as_view(), name='user-posts'),
    path('api-token-auth/', drf_auth_views.obtain_auth_token),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
    path('categories/<int:category_id>/topics/', views.CategoryTopicsList.as_view(), name='category-topics'),
] + debug_toolbar_urls()
