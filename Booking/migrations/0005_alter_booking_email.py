# Generated by Django 5.0.3 on 2024-06-30 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0004_alter_booking_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=250, null=True),
        ),
    ]
