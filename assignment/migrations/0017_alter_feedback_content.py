# Generated by Django 5.1.2 on 2024-11-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0016_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=models.TextField(),
        ),
    ]
