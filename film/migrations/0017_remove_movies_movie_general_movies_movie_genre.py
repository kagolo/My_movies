# Generated by Django 4.1.2 on 2023-01-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0016_plan_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='movie_general',
        ),
        migrations.AddField(
            model_name='movies',
            name='movie_genre',
            field=models.CharField(choices=[('ACTION', 'ACTION'), ('HORROR', 'HORROR'), ('SCIENCE FRICTION', 'SCIENCE FRICTION'), ('LOVE STORY', 'LOVE STORY'), ('INDIAN', 'INDIAN')], default='ACTION', max_length=300),
        ),
    ]
