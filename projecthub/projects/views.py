from django.http.response import HttpResponse

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.shortcuts import render,redirect
from .models import Project

from .forms import ProjectsForm
from .forms import NewUserForm

#new
from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate, logout

#new
from .utils import searchProjects

# Create your views here.

def home(request):
    return render(request,'home.html')

def projects(request):
    projects, search_query = searchProjects(request)

    context = {'projects': projects,
               'search_query': search_query}
    # all_project = Project.objects.all()
    # context = {'projects':all_project}
    return render(request,'projects/projects.html',context)
    
def project_detail(request,project_id):
    project = Project.objects.get(id=project_id)
    context = {'project' : project}
    return render(request,'projects/single-project.html',context)

def create_project(request):
    form = ProjectsForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ProjectsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request,'projects/project-form.html',context)

def edit_project(request,project_id):
    project = Project.objects.get(id=project_id)
    form = ProjectsForm(instance=project)
    context = {'form':form}

    if request.method == 'POST':
        form = ProjectsForm(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request,'projects/project-form.html',context)


def delete_project(request,project_id):
    obj = get_object_or_404(Project, id = project_id)
    all_project = Project.objects.all()
    context = {'projects':all_project}

    if request.method == 'POST':
        
        obj.delete()
        return redirect('projects')
    return render(request,'projects/delete-project.html',context)

#new


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('projects')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="projects/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('projects')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'projects/login.html', context={"login_form":form})
    #new
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('home')


def store(request):
	context = {}
	return render(request, 'projects/store.html', context)

def cart(request):
	context = {}
	return render(request, 'projects/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'projects/checkout.html', context)