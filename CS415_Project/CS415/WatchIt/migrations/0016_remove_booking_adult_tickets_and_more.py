# Generated by Django 4.2.3 on 2024-04-22 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WatchIt', '0015_booking_adult_tickets_booking_child_tickets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='adult_tickets',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='child_tickets',
        ),
    ]
