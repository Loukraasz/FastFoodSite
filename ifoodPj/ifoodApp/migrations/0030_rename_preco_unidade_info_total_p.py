# Generated by Django 4.2.5 on 2023-12-16 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0029_info_preco_unidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='preco_unidade',
            new_name='total_p',
        ),
    ]
