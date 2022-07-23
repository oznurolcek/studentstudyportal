"""studentstudyportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = "index"),
    path('user/',include("user.urls")),

    #notes
    path('notes/', include("note.urls")),

    #homeworks
    path('homeworks/',views.homeworks, name = "homeworks"),
    path('update_homeworks/<int:pk>',views.update_homeworks,name="update-homeworks"),
    path('delete_homeworks/<int:pk>',views.delete_homeworks,name="delete-homeworks"),
    
    #exammarks
    path('exammarks/',views.exammarks, name = "exammarks"),
    path('update_exammarks/<int:pk>',views.update_exammarks,name="update-exammarks"),
    path('delete_exammarks/<int:pk>',views.delete_exammarks,name="delete-exammarks"),

    #examcalendar
    path('examcalendar/',views.examcalendar, name = "examcalendar"),
    path('update_calendar/<int:pk>',views.update_examcalendar,name="update-examcalendar"),
    path('delete_calendar/<int:pk>',views.delete_examcalendar,name="delete-examcalendar"),

    #todolist
    path('todolist/',views.todolist, name = "todolist"),
    path('update_todo/<int:pk>',views.update_todo,name="update-todo"),
    path('delete_todo/<int:pk>',views.delete_todo,name="delete-todo"),

    #timer
    path('timer/',views.timer, name = "timer"),

    #askquestion
    path('questions/',views.questions, name = "questions"),
    path('askquestion/',views.askquestion, name = "askquestion"),
    path('question_detail/<int:id>',views.question_detail, name = "question_detail"),
    path('question_delete/<int:id>',views.question_delete, name = "question_delete"),
    path('comment/<int:id>',views.addComment, name = "comment"),
    

    #music
    path('music/',views.music, name = "music"),

        
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
