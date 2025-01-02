from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('add_book/', views.add_book, name='add_book'),
    path('read/<int:book_id>/', views.read_book, name='read_book'),
]
