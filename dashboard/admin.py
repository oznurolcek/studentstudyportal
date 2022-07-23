from django.contrib import admin
from .models import Examcalendar, Exammarks, Homework, ToDo, Question, Comment
# Register your models here.

#admin.site.register(ToDo)
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ["title","user","is_finished"]
    class Meta:
        model = ToDo

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ["user","subject","description","due","is_finished"]
    class Meta:
        model = Homework

@admin.register(Exammarks)
class ExammarksAdmin(admin.ModelAdmin):
    list_display = ["user","subject","firstExam","secondExam","final","average"]
    class Meta:
        model = Exammarks

@admin.register(Examcalendar)
class ExamcalendarAdmin(admin.ModelAdmin):
    list_display = ["user","subject","examDate","examHour","is_finished"]
    class Meta:
        model = Examcalendar

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date"]
    list_display_links = ["title"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Question

admin.site.register(Comment)

