# Generated by Django 4.1.2 on 2023-04-06 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0024_alter_movies_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movie_status1',
            field=models.CharField(choices=[('New Movie', 'New Movie'), ('Featured', 'Featured')], default='New', max_length=300),
        ),
    ]
