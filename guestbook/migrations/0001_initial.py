# Generated by Django 3.2 on 2021-06-16 00:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('passwd', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
