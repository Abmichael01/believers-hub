# Generated by Django 4.2.11 on 2024-03-25 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_visits_count'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visits',
            new_name='Visit',
        ),
    ]
