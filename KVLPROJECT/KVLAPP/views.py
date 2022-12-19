from django.shortcuts import render
from django.http import HttpResponse
def hi(request):
    #return HttpResponse("<h1>this is my home page</h1>")
     return render(request,'KVLAPP/k.html')
# Create your views here.
