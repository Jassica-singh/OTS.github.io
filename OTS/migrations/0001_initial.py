# Generated by Django 4.1.7 on 2023-05-08 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('test_attempted', models.IntegerField()),
                ('points', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('que', models.TextField()),
                ('a', models.CharField(max_length=255)),
                ('b', models.CharField(max_length=255)),
                ('c', models.CharField(max_length=255)),
                ('d', models.CharField(max_length=255)),
                ('ans', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('resultid', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
                ('attempt', models.IntegerField()),
                ('right', models.IntegerField()),
                ('wrong', models.IntegerField()),
                ('points', models.FloatField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OTS.candidate')),
            ],
        ),
    ]
