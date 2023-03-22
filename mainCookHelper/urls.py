from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.login, name='login'),
    path('post/<int:pk>/', views.recept_detail, name='recept_detail'),
    path('post/new/', views.recept_new, name='recept_new'),
    path('post/<int:pk>/edit/', views.recept_edit, name='recept_edit'),
    path('post/<int:pk>/delete/', views.recept_delete, name='recept_delete'),
    path('accounts/logout/', views.logout, name='logout'),
]