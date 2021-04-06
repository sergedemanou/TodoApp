from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_todos_items, name= "list_todos_items"),
    path('insert_todo/', views.insert_todos_items, name= "insert_todos_items"),
    path('delete_todo/<int:pk>/', views.delete_item, name= "delete_item"),
]
