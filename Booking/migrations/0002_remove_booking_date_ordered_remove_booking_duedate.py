# Generated by Django 5.0.3 on 2024-06-30 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date_ordered',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='dueDate',
        ),
    ]
