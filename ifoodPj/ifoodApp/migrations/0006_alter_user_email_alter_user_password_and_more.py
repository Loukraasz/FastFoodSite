# Generated by Django 4.2.5 on 2023-10-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0005_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.IntegerField(null=True),
        ),
    ]
