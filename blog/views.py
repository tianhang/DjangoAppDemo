from django.shortcuts import render
from django.http import HttpRequest
from blog.models import BlogPost
# Create your views here.

def archive(request):
    post_list = BlogPost.objects.all()
    context = {'posts':post_list}
    return render(request,'archive.html',context)

