# Generated by Django 3.2.5 on 2021-07-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
