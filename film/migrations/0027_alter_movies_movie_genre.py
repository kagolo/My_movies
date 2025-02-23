# Generated by Django 4.1.2 on 2024-11-14 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0026_series_serie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movie_genre',
            field=models.CharField(choices=[('SUPER ACTION', 'SUPER ACTION'), ('ACTION COMEDY', 'ACTION COMEDY'), ('ROMANTIC ACTION', 'ROMANTIC ACTION'), ('HORROR THRILLER', 'HORROR THRILLER'), ('SCIENCE FRICTION', 'SCIENCE FRICTION'), ('LOVE STORY', 'LOVE STORY'), ('INDIAN', 'INDIAN'), ('ACTION DETECTIVE', 'ACTION DETECTIVE'), ('COMEDY', 'COMEDY'), ('ROMANTIC COMEDY', 'ROMANTIC COMEDY'), ('ADVENTURE', 'ADVENTURE'), ('ENGLISH', 'ENGLISH'), ('CARTOON', 'CARTOON')], default='ACTION', max_length=300),
        ),
    ]
