# Generated by Django 4.2.2 on 2023-06-21 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('sender', models.CharField(max_length=32)),
                ('number_of_stars', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
