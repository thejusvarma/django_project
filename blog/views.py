from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Thejus',
        'title':'Hello',
        'content':'hfwefhwefwfnwff',
        'date_posted':'aug 25'
    },
    {
        'author':'shreya',
        'title':'wworld',
        'content':'hfdffhwefwfnwff',
        'date_posted':'aug 29'
    }
]

def home(request):
    context =  {
        'posts': posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
# Create your views here.
