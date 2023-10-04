# Generated by Django 4.2.5 on 2023-10-04 20:37

from django.db import migrations, models
import ifoodApp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0002_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=40, validators=[ifoodApp.validators.validate_even]),
        ),
    ]
