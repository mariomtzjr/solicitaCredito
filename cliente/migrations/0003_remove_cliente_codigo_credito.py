# Generated by Django 2.2.1 on 2019-05-21 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_remove_cliente_solicitud'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='codigo_credito',
        ),
    ]
