# Generated by Django 3.2.9 on 2022-01-03 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_notesrating_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='notesrating',
            name='votes_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='NotesRatingVotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('notes_rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='notes.notesrating', unique=True)),
            ],
        ),
    ]