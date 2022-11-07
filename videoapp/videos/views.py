from django.shortcuts import render
from .models import Category,Video

def  home(request):
    data ={
        "kategoriler":Category.objects.all(),
        "videolar":Video.objects.filter(anasayfa=True)
    }
    return render(request,"index.html",data)


def  videos(request):
    data ={
        "kategoriler":Category.objects.all(),
        "videolar":Video.objects.all()
    }
    return render(request,"videos.html",data)

def  videodetails(request,id):
    data ={
        "video":Video.objects.get(id=id)
    }
    return render(request,"details.html",data)
