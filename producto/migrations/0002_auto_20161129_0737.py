# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-29 07:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'permissions': (('view_producto', 'Puede ver la lista de productos'),), 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
    ]