# Generated by Django 3.2.9 on 2022-01-08 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_contentgroupuserprogress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseuserprogress',
            name='last_content_group',
        ),
    ]
