from django.urls import path
from . import views


app_name = 'home'

urlpatterns = [
    path('', views.HomeView, name='index'),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('posts/', views.PoststView, name='posts'),
    path('post/<int:post_id>/', views.DetailstView, name='details'),
    path('posts/create/', views.CreatePostView, name='create'),
    path('posts/delete/<int:post_id>/', views.DeletePostView, name='delete'),
    path('posts/update/<int:post_id>/', views.UpdatePostView, name='update'),
]
