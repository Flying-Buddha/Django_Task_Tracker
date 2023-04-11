from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from account.models import Task, Project
from .forms import TaskForm, ProjectForm


# -----------Register User
def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
            # check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is been used')
                    return redirect('register')
                else:
                    # looks good
                    user =User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'pages/register.html')

# ---------Authenticate and Login
def login(request):
    if request.method == 'POST':
        # Login User
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'pages/login.html')

#--------User Logout
def logout(request):
   if request.method == 'POST':
      auth.logout(request)
      messages.success(request, 'You are now logged out')
   return redirect('login')

# Render dashboard and View All datatabe
@login_required
def dashboard(request):
    task_list = Task.objects.all()
    critical_tasks = Task.objects.filter(priority='Critical').count()
    completed_tasks = Task.objects.filter(status='Completed').count()
    readygo_tasks = Task.objects.filter(status='Ready to go').count()

    total_tasks = Task.objects.count()
    if total_tasks > 0:
        percentage_completed = round((completed_tasks / float(total_tasks)) * 100)
    else:
        percentage_completed = 0

    context ={
        'taskslist':task_list, 
        'readygo_tasks':readygo_tasks, 
        'readygo_tasks':readygo_tasks, 
        'critical_tasks':critical_tasks, 
        'completed_tasks':completed_tasks,
        'percentage_completed':percentage_completed}

    return render(request, 'pages/dashboard.html', context)

# -----------Create a Task
@login_required
def createTask(request):
    TableTitle = "Create A Task"
    form = TaskForm()
    if request.method == "POST":
        print('Printing POST:', request.POST )
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your task has been created')
            return redirect('dashboard')

    context ={'form':form, 'TableTitle':TableTitle}
    return render (request, 'pages/task_form.html', context)


# -----------Create a Project
@login_required
def createProject(request):
    TableTitle = "Add A Project"
    form = ProjectForm()
    if request.method == "POST":
        print('Printing POST:', request.POST )
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Added')
            return redirect('dashboard')

    context ={'form':form, 'TableTitle':TableTitle}
    return render (request, 'pages/task_form.html', context)

#------------ Update a Task
@login_required
def update_task(request, pk):
    TableTitle = "Update A Task"
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Updated')
            return redirect('dashboard')

    context = {'form':form, 'TableTitle':TableTitle}
    return render(request, 'pages/task_form.html', context)

#------------ Delete a Task
@login_required
def delete_task(request, pk):       
    task = Task.objects.get(id=pk)
    task.delete()
    messages.success(request, 'The record has been deleted')
    return redirect('dashboard')

#------------ User Task List
@login_required
def your_tasks(request):
    owner_username = request.user.username
    tasks = Task.objects.filter(owner__username=owner_username)

    critical_tasks = Task.objects.filter(priority='Critical', owner__username=owner_username).count()
    completed_tasks = Task.objects.filter(status='Completed', owner__username=owner_username).count()
    readygo_tasks = Task.objects.filter(status='Ready to go', owner__username=owner_username).count()
    print(completed_tasks)

    total_tasks = Task.objects.count()

    if total_tasks > 0:
        percentage_completed = round((completed_tasks / float(total_tasks)) * 100)
    else:
        percentage_completed = 0
    print(percentage_completed)

    context ={
        'tasks':tasks, 
        'readygo_tasks':readygo_tasks, 
        'readygo_tasks':readygo_tasks, 
        'critical_tasks':critical_tasks, 
        'completed_tasks':completed_tasks,
        'percentage_completed':percentage_completed}

    return render(request, 'pages/profile.html', context)
