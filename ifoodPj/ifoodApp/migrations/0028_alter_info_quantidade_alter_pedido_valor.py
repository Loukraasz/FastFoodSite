# Generated by Django 4.2.5 on 2023-12-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0027_remove_cart_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='quantidade',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor',
            field=models.FloatField(null=True),
        ),
    ]
