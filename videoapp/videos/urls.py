from django.urls import path
from . import views
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/videos
# http://127.0.0.1:8000/videos/1
# http://127.0.0.1:8000/videos/video-1
urlpatterns =[
    
    path("",views.home,name="home"),
    path("home",views.home),
    path("videos",views.videos,name="videos"),
     path("videos/<int:id>",views.videodetails,name="details"),

]