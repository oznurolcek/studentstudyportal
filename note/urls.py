from django.contrib import admin
from django.urls import path
from . import views

app_name = "note"

urlpatterns = [
    path('mynotes/', views.mynotes, name = "mynotes"),
    path('addnote/', views.addnote, name = "addnote"),
    path('note/<int:id>', views.detail, name = "detail"),
    path('update/<int:id>', views.updateNote, name = "update"),
    path('delete/<int:id>', views.deleteNote, name = "delete"),
    path('', views.notes, name = "notes"),
]