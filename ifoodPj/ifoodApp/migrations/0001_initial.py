# Generated by Django 4.2.5 on 2023-10-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.IntegerField()),
            ],
        ),
    ]
