# Generated by Django 4.2.5 on 2023-12-15 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0023_remove_cart_quantidade_quantidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='quantidades',
            name='carrinho',
            field=models.ManyToManyField(to='ifoodApp.cart'),
        ),
    ]
