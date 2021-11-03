from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World!</h1>")

def bootstrap(request):
    my_dict = {'insert_me':"Hello, views.py"}
    return render(request,'bootstrap1.html',context=my_dict)
