from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey


# Create your models here
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()

    def __str__(self):
        return self.name


class Task(models.Model):
    
    priority_choice= [
    ('Critical', 'Critical'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
    ('Best Effort', 'Best effort'),
    ]

    status_choice= [
    ('Ready to go', 'Ready to go'),
    ('In progress', 'In progress'),
    ('Completed', 'Completed'),
    ('stuck', 'Stuck'),
    ]

    owner = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL, null='TRUE')
    #owner = models.ForeignKey(User, on_delete=models.SET_NULL, null='TRUE')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    details = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=100, null=True, choices=priority_choice)
    status = models.CharField(max_length=100, null=True, choices=status_choice)

    def __str__(self):
        return self.title