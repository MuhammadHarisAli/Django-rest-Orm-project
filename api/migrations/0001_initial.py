# Generated by Django 4.0.3 on 2022-03-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Creation date')),
                ('channel', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=200)),
                ('impressions', models.SmallIntegerField()),
                ('clicks', models.SmallIntegerField()),
                ('installs', models.SmallIntegerField()),
                ('spend', models.FloatField()),
                ('revenue', models.FloatField()),
            ],
        ),
    ]