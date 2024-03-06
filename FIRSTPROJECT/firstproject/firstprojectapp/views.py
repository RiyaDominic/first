from django.http import HttpResponse
from django.shortcuts import render
from  .models import Info

# Create your views here.
def demo(request):
    obj=Info.objects.all()
    return render(request,"index.html",{'result':obj})


