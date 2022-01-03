# Generated by Django 3.2.9 on 2022-01-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20220101_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='category',
            new_name='categories',
        ),
        migrations.RemoveField(
            model_name='notescategory',
            name='count',
        ),
        migrations.AddField(
            model_name='notesrating',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]