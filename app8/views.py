from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from app8.utilities import store_img


# Create your views here.
def img_upld(request):
    return render(request,"img_upld.html")

def img_disp(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        img1=request.FILES.get('sam1')
        img2=request.FILES.get('sam2')
        file_urls=map(store_img,[img1,img2])
    
    return render(request,"img_disp.html",context={'file_urls':file_urls})
