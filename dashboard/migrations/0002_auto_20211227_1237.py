# Generated by Django 3.2.9 on 2021-12-27 12:37

import dashboard.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.AddField(
            model_name='course',
            name='profile_image',
            field=models.ImageField(blank=True, default='banner/banner.png', max_length=255, null=True, upload_to=dashboard.models.get_course_banner_filepath),
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('progress', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('course', models.ManyToManyField(related_name='user', to='dashboard.Course')),
                ('user', models.ManyToManyField(related_name='course', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
