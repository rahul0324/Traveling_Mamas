# Generated by Django 2.2 on 2019-10-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravellingMamas', '0007_auto_20191026_0822'),
    ]

    operations = [
        migrations.CreateModel(
            name='flight_prime',
            fields=[
                ('flight_code', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('arrival_time', models.CharField(max_length=100)),
                ('departure_time', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]
