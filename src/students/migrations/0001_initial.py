# Generated by Django 3.0.5 on 2020-04-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('roll_no', models.IntegerField(max_length=100)),
                ('gender', models.CharField(max_length=120)),
                ('dob', models.DateField(default='1998-01-01')),
                ('grade', models.IntegerField(max_length=100)),
                ('father_name', models.CharField(max_length=120)),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
