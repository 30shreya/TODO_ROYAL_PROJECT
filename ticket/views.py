from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    print("addticket app ")
    return HttpResponse("add ticket called..")

def view(request):
    return HttpResponse("view ticket called..")
def mainpage(request):
    return render(request, 'ticket/mainpage.html')