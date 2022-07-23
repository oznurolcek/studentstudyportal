from django.db import models
from decimal import *

from django.db.models.deletion import CASCADE

# Create your models here.

class ToDo(models.Model):
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name='Görev')
    is_finished = models.BooleanField(default=False,verbose_name='Tamamlandı mı?')
    def __str__(self):
        return self.title

class Homework(models.Model):
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    subject = models.CharField(max_length=50,verbose_name='Ders')
    description = models.TextField(verbose_name='İçerik')
    due = models.DateTimeField(verbose_name='Son Tarih')
    is_finished = models.BooleanField(default=False,verbose_name='Tamamlandı mı?')
    def __str__(self):
        return self.description

class Exammarks(models.Model):
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    subject = models.CharField(max_length=50,verbose_name='Ders')
    firstExam = models.FloatField(default=0.0,verbose_name='Birinci Vize')
    secondExam = models.FloatField(default=0.0,verbose_name='İkinci Vize')
    final = models.FloatField(default=0.0,verbose_name='Final')  
    average = models.IntegerField(default=0,verbose_name='Ortalama')
    def __str__(self):
        return self.subject

class Examcalendar(models.Model):
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    subject = models.CharField(max_length=50,verbose_name='Ders')
    examDate = models.DateTimeField(verbose_name='Sınav Tarihi')
    examHour = models.TimeField(verbose_name='Sınav Saati')
    is_finished = models.BooleanField(default=False,verbose_name='Tamamlandı mı?')
    def __str__(self):
        return self.subject

class Question(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    title = models.CharField(max_length = 50, verbose_name = "Soru Başlığı")
    content = models.TextField(verbose_name = "Soru")
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = "Oluşturulma Tarihi")
    def _str_(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE, verbose_name = "Soru", related_name = "comments")
    comment_author = models.CharField(max_length = 50, verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200, verbose_name = "Cevap")
    comment_date = models.DateTimeField(auto_now_add = True)
    def _str_(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']