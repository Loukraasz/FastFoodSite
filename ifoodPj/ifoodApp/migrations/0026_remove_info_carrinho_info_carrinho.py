# Generated by Django 4.2.5 on 2023-12-16 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0025_rename_quantidades_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='carrinho',
        ),
        migrations.AddField(
            model_name='info',
            name='carrinho',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ifoodApp.cart'),
        ),
    ]