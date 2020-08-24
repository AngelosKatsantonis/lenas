# Generated by Django 3.1 on 2020-08-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=40)),
                ('latitude', models.CharField(max_length=40)),
                ('longitude', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ['area'],
            },
        ),
    ]
