# Generated by Django 3.2.5 on 2021-08-03 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('Hotel_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Hotel_title', models.CharField(max_length=50)),
                ('price', models.JSONField()),
                ('image', models.ImageField(upload_to='')),
                ('location', models.CharField(max_length=75)),
            ],
        ),
    ]
