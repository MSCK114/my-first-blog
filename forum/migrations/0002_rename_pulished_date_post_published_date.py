# Generated by Django 4.2.7 on 2023-11-17 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pulished_date',
            new_name='published_date',
        ),
    ]
