from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages
import datetime
from time import strftime, localtime,gmtime
from django.utils import timezone



def index(request):
    return render(request,'ext_app/index.html')


def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request,err)
        return redirect('/')
    request.session['user_id'] = result.id
    #print result.id
    # messages.success(request, "Successfully registered!")
    return redirect('/show_dashboard')


def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    # messages.success(request, "Successfully logged in!")
    return redirect('/show_dashboard')


def show_dashboard(request):
    content = {
        'user' : User.objects.get(id = request.session['user_id']),
        'products':User.objects.get(id = request.session['user_id']).joined.all(),
        'alls': Travel.objects.exclude(added_by_id =request.session['user_id']) 
        
    }
    
    return render(request,'ext_app/dashboard.html',content)

def add_show(request,id):
    
    content = {
        'user' : User.objects.get(id = id)
    }
    return render(request,'ext_app/create.html',content)


def create_list(request):
    
   
    user_id= request.session['user_id']
    content = {
        'user' : User.objects.get(id = request.session['user_id'])
    }

    if len(request.POST['destination']) < 1 or len(request.POST['description']) < 1 or len(request.POST['start_date']) < 1 or len(request.POST['end_date']) < 1:
        messages.error(request,'No Empty Entries Pls')
        return redirect('/travels/add/'+ str(user_id)  )

    start_date = request.POST['start_date']
    end_date = request.POST['end_date']
    if end_date < start_date:
        messages.error(request,'End date should be greater than start date.')
        return redirect('/travels/add/'+ str(user_id)  )


    

       
    user = User.objects.get(id = request.session['user_id'])
    l = Travel.objects.create(destination = request.POST['destination'],
    plan = request.POST['description'],
    start_date = request.POST['start_date'],
    end_date = request.POST['end_date'],
    added_by = user)
    l.joined_by.add(user)
    return redirect('/show_dashboard')


def show_travellist(request,id):
    
    content = {
        
        'products' : Travel.objects.get(id = id),
        'users' : Travel.objects.get(id = id).joined_by.all()  
        
       
    }
    return render(request,'ext_app/show.html',content)


def add_list(request ,id):
    list = Travel.objects.get(id= id)
    user = User.objects.get(id = request.session['user_id'])
    list.joined_by.add(user)
    return redirect('/show_dashboard')