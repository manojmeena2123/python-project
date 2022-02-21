from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def xyz(request):
    return render(request, "index.html")

def signup(request):
    print(signup is working)
    return render(request, "index.html")
