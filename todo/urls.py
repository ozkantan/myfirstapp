from django.urls import path
from . import views

urlpatterns = [
    path('', views.todoapp),
    path('todoadd/', views.todoadd),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]