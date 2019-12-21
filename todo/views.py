from django.shortcuts import render,redirect,get_object_or_404
from .models import TodoAppTheme
from datetime import datetime, timezone
from time import strftime,sleep
from django.core.mail import send_mail



# Create your views here.

def todoapp(request):
    todos = TodoAppTheme.objects.all()
 
    return render(request,"index.html",{"todos":todos})

def todoadd(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get("title")
        email = request.POST.get("email")
        send_date = request.POST.get("send_date")
        print(send_date)
        newtodo = TodoAppTheme(title = title, completed = False, taskdurum= False, email = email, send_date = send_date)
        newtodo.save()
        return redirect("/")
        

def update(request,id):
    # todo = TodoAppTheme.objects.filter(id = id).first()
    todo = get_object_or_404(TodoAppTheme, id = id)
    todo.completed = not todo.completed  
    todo.save() 
    return redirect("/")

def delete(request,id):
    todo = get_object_or_404(TodoAppTheme, id = id)
    todo.delete()
    return redirect("/")

def tasktodo(request, id):
    todo = get_object_or_404(TodoAppTheme, id = id)
    todo.taskdurum = not todo.taskdurum
    todo.save()

    # print(todo.taskdurum)

    # print(todo.id)
    # print(str(todo.send_date).replace("+00:00",""))
    tarihtask = str(todo.send_date).replace("+00:00","")
    simdi = strftime("%Y-%m-%d %H:%M:%S")
    # print(tarihtask)
    # print(simdi)
    if tarihtask < simdi:
        return redirect("/")
    if todo.taskdurum:
        while True:
            simdi = strftime("%Y-%m-%d %H:%M:%S")
            # print(tarihtask)
            print(simdi)
            if tarihtask == simdi:
                send_mail('Hatırlatma Maili Önemli', todo.title, 'mail adress', [todo.email])
                sleep(1)
                return redirect("/")
                
    
    return redirect("/")
    # 2019-12-19 23:13:40+00:00
    


