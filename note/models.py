from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Note(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    title = models.CharField(max_length = 50, verbose_name = "Başlık")
    content = RichTextField(verbose_name = "İçerik")
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = "Oluşturulma Tarihi")
    note_image = models.FileField(blank = True, null = True, verbose_name = "Fotoğraf Ekle")
    def __str__(self):
        return self.title