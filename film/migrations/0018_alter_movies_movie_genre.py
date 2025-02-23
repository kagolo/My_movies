# Generated by Django 4.1.2 on 2023-01-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0017_remove_movies_movie_general_movies_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movie_genre',
            field=models.CharField(choices=[('ACTION', 'ACTION'), ('HORROR', 'HORROR'), ('SCIENCE FRICTION', 'SCIENCE FRICTION'), ('LOVE STORY', 'LOVE STORY'), ('INDIAN', 'INDIAN'), ('COMEDY', 'COMEDY')], default='ACTION', max_length=300),
        ),
    ]
