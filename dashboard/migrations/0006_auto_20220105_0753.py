# Generated by Django 3.2.9 on 2022-01-05 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20211231_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercourse',
            name='course',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='user',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='UserCourse',
        ),
    ]