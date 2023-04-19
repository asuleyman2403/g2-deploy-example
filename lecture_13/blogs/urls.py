from blogs.views import home_page, create_blog, blog_details, create_post, post_details_page, delete_post, delete_blog
from django.urls import path

urlpatterns = [
    path('', home_page, name='home_page'),
    path('blogs/create/', create_blog, name='create_blog'),
    path('blogs/<int:pk>/', blog_details, name='blog_details'),
    path('blogs/<int:pk>/create-post/', create_post, name='create_post'),
    path('blogs/<int:pk>/delete/', delete_blog, name='delete_blog'),
    path('posts/<int:pk>/', post_details_page, name='post_details_page'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post')
]
