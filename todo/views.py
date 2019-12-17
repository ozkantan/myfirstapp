from django.shortcuts import render,redirect,get_object_or_404
from .models import TodoAppTheme

# Create your views here.
def todoapp(request):
    todos = TodoAppTheme.objects.all()
    return render(request,"index.html",{"todos":todos})

def todoadd(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get("title")
        newtodo = TodoAppTheme(title = title, completed = False)
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
