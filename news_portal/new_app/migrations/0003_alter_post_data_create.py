# Generated by Django 5.2 on 2025-05-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_alter_author_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_create',
            field=models.DateField(),
        ),
    ]
