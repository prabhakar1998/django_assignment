# Generated by Django 3.2.3 on 2021-07-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_area', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicearea',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='servicearea',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='serviceprovider',
            name='date_updated',
        ),
        migrations.AddField(
            model_name='servicearea',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]