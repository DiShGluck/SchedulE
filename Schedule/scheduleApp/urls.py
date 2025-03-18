from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login_teacher, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add/', views.add_schedule, name='add_schedule'),
    path('update/<int:pk>/', views.update_schedule, name='update_schedule'), 
    path('delete/<int:pk>/', views.delete_schedule, name='delete_schedule'), 
    path('add-group/', views.add_group, name='add_group'),
    path('add-subject/', views.add_subject, name='add_subject'),
    path('add-teacher/', views.add_teacher, name='add_teacher'),
]