# Generated by Django 4.0 on 2022-01-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_examcalendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='examcalendar',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name='Tamamlandı mı?'),
        ),
    ]
