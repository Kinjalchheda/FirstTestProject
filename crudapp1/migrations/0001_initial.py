# Generated by Django 4.1 on 2022-08-26 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
                ('ecity', models.CharField(max_length=100)),
                ('esalary', models.IntegerField(default=0)),
            ],
        ),
    ]
