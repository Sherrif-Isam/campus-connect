# Generated by Django 4.2.11 on 2024-03-06 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_alter_event_options_remove_event_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_host_time_AMPM',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=2),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_host_time',
            field=models.IntegerField(choices=[(1, '1:00'), (2, '2:00'), (3, '3:00'), (4, '4:00'), (5, '5:00'), (6, '6:00'), (7, '7:00'), (8, '8:00'), (9, '9:00'), (10, '10:00'), (11, '11:00'), (12, '12:00')], default=1),
        ),
    ]