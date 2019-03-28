# Generated by Django 2.1.7 on 2019-03-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uName', models.CharField(max_length=25)),
                ('brightness', models.IntegerField(default=100)),
                ('ColorTemp', models.IntegerField(default=2700)),
                ('hue', models.IntegerField()),
                ('address', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('sat', models.IntegerField()),
                ('ip', models.CharField(max_length=25)),
            ],
        ),
    ]
