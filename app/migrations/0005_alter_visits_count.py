# Generated by Django 4.2.11 on 2024-03-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_visits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
