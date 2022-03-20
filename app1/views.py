from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

# Create your views here.
def xyz(request):
    return render(request, "index.html")

def signUp(request):
    email = request.GET['email']
    psw = request.GET['psw']
    cursor = connection.cursor()
    query = "insert into users (email, password) values(%s,  %s)"
    value = (email, psw)
    cursor.execute(query, value)

    # query = ''' select*from student'''
    # cursor.execute(query)
    # row = cursor.fetchone()
    # print(row)
    data = {"email":email, "password":psw}
    return render(request, "second.html", data)

