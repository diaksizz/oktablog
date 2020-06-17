from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth

from  posts.models import Posts



def home(request):
    title ='Home'
    posts = Posts.objects.all()
    return render(request,'index.html',{'title':title,'posts':posts,})

def about(request):
    title='about'
    return render(request,'about.html',{'title':title})
    

def logout(request):
    auth.logout(request)
    return redirect('/')