from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login_teacher, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add/', views.add_schedule, name='add_schedule'),
    path('update/<int:pk>/', views.update_schedule, name='update_schedule'), 
    path('delete/<int:pk>/', views.delete_schedule, name='delete_schedule'), 
]