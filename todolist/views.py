from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.forms import Form
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.filter(user=request.user)
    context = {
        'list_task': data_task
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', task), content_type='application/json')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = Form(request.POST)
    if request.method == 'POST':
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        return redirect('todolist:show_todolist')
    context = {'form': form}
    return render(request, "create-task.html", context)

def ubah_status(request, id):
    status = Task.objects.get(pk=id)
    if status.is_finished:
        status.is_finished = False
    else:
        status.is_finished = True
    status.save()
    return redirect('todolist:show_todolist')

def hapus_task(request, id):
    hapus = Task.objects.get(pk=id)
    hapus.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_ajax(request):
    if request.method == 'POST':
        date = datetime.datetime.now()
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        task = Task(user=user, date=date, title = title, description = description)
        task.save()

        output = {
            'pk':task.pk,
            'fields':{
                'title':task.title,
                'description':task.description,
                'is_finished':task.is_finished,
                'date':task.date,
            }
        }
        return JsonResponse(output)

@csrf_exempt
def delete_ajax(request,id):
    task = Task.objects.filter(pk=id)   
    task.delete()
    return JsonResponse({"task": "task dihapus"})