# Generated by Django 5.0.6 on 2024-05-31 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_category_options_alter_movie_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actor',
            new_name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='update_at',
        ),
    ]
