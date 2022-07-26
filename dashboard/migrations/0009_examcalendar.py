# Generated by Django 4.0 on 2022-01-02 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('dashboard', '0008_alter_exammarks_average'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examcalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='Ders')),
                ('examDate', models.DateTimeField(verbose_name='Sınav Tarihi')),
                ('examHour', models.TimeField(verbose_name='Sınav Saati')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
