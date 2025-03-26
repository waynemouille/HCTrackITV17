from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import AddKnowledgebaseForm, UpdateKnowledgebaseForm






# KNOWLEDGE BASE HOME PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def knowledgebaseHome(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('knowledgebase_home')
        else:
            messages.warning(request, "There was a problem logging in.  Please try again.")
            return redirect('login')
    else:
        return render (request, 'knowledgebase_home.html', {'articles':articles})
#------------------------------------------------------------------------------------------------------------------------#




# CREATE NEW KNOWLEDGE BASE ARTICLE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def knowledgebaseCreatenew(request):
    form = AddKnowledgebaseForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                instance = form.save(commit=False)
                instance.created_by = request.user
                instance.save()
                return redirect('knowledgebase_home')
        return render (request, 'knowledgebase_createnew.html', {'form':form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('login')
#------------------------------------------------------------------------------------------------------------------------#



# KNOWLEDGE BASE ARTICLE INFORMATION PAGE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def knowledgebaseInfo(request, pk):
    article = Article.objects.get(id=pk)


    context = {'article':article}
    return render(request, 'knowledgebase_info.html', context)


def knowledgebaseDelete(request, pk):
    delete_it = Article.objects.get(id=pk)
    delete_it.delete()
    context = {}
    return render(request, 'knowledgebase_delete.html', context)
#------------------------------------------------------------------------------------------------------------------------#

# EDIT KNOWLEDGE BASE ARTICLE
#------------------------------------------------------------------------------------------------------------------------#
@login_required(login_url='login')
def knowledgebaseEdit(request, pk):
    article = Article.objects.get(id=pk)
    form = UpdateKnowledgebaseForm(instance=article)
    if request.method == "POST":
        form = UpdateKnowledgebaseForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('knowledgebase_home')

    context = {'form':form}
    return render(request, 'knowledgebase_edit.html', context)
#------------------------------------------------------------------------------------------------------------------------#