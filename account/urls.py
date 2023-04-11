from django.urls import path
from .import views

# Rending URL paths to render documents and call views
urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create_task', views.createTask, name="create_task"),
    path('create_project', views.createProject, name="create_project"),
    path('update_task/<str:pk>', views.update_task, name="update_task"),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    path('your_tasks', views.your_tasks, name='your_tasks')
]