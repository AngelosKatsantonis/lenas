# Generated by Django 3.1 on 2020-08-22 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.CharField(default='Please provide a simple description of your case and your goals.', max_length=250),
        ),
    ]