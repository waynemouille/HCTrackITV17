from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import AddProjectForm, UpdateProjectForm, CompleteProjectForm




# ALL PROJECTS PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def projectsHome(request):
    projects = Project.objects.all().order_by('-created_at')
    projects = projects.filter(Q(progress='0%')
                             | Q(progress='10%')
                             | Q(progress='20%')
                             | Q(progress='30%')
                             | Q(progress='40%')
                             | Q(progress='50%')
                             | Q(progress='60%')
                             | Q(progress='70%')
                             | Q(progress='80%')
                             | Q(progress='90%')                      
                             )
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('projects_home')
        else:
            messages.warning(request, "There was a problem logging in.  Please try again.")
            return redirect('login')
    else:
        return render (request, 'projects_home.html', {'projects':projects})
#------------------------------------------------------------------------------------------------------------------------#


# COMPLETED PROJECTS PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def projectsCompleted(request):
    projects = Project.objects.all().order_by('-created_at')
    projects = projects.filter(Q(progress='100%')                       
                             )
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('projects_completed')
        else:
            messages.warning(request, "There was a problem logging in.  Please try again.")
            return redirect('login')
    else:
        return render (request, 'projects_completed.html', {'projects':projects})
#------------------------------------------------------------------------------------------------------------------------#


# CREATE NEW PROJECT
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def projectsCreatenew(request):
    form = AddProjectForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                instance = form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                return redirect('projects_home')
        return render (request, 'projects_createnew.html', {'form':form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('login')
#------------------------------------------------------------------------------------------------------------------------#



# PROJECT INFORMATION PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def projectsInfo(request, pk):
    projects = Project.objects.get(id=pk)


    context = {'project':projects}
    return render(request, 'projects_info.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# UPDATE PROJECT
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def projectsUpdate(request, pk):
    ticket = Project.objects.get(id=pk)
    form = UpdateProjectForm(instance=ticket)
    if request.method == "POST":
        form = UpdateProjectForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('projects_home')

    context = {'form':form}
    return render(request, 'projects_update_update.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# COMPLETE PROJECT
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def completeProject(request, pk):
    ticket = Project.objects.get(id=pk)
    form = CompleteProjectForm(instance=ticket)
    if request.method == "POST":
        form = CompleteProjectForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('projects_home')

    context = {'form':form}
    return render(request, 'projects_update_complete.html', context)
#------------------------------------------------------------------------------------------------------------------------#


# COMPLETED PROJECT INFORMATION PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def projectsCompletedinfo(request, pk):
    project = Project.objects.get(id=pk)


    context = {'project':project}
    return render(request, 'projects_info_completed.html', context)
#------------------------------------------------------------------------------------------------------------------------#