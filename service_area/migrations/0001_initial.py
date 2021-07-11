# Generated by Django 3.2.3 on 2021-07-10 20:22

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Service Provider Name')),
                ('email', models.EmailField(max_length=150, verbose_name='Service Provider Email')),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('language', models.CharField(default='en-us', max_length=50)),
                ('currency', models.CharField(default='USD', max_length=50)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Service Area Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service_area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='service_area.serviceprovider')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
