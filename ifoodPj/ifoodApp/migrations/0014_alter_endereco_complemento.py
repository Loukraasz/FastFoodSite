# Generated by Django 4.2 on 2023-11-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0013_alter_endereco_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
