# Generated by Django 3.0.3 on 2020-06-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('fullname', models.CharField(max_length=50)),
                ('emp_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
    ]
