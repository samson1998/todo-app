# Generated by Django 3.0 on 2020-07-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateField(default='2020-07-01'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default='2020-07-01'),
        ),
    ]
