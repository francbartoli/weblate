# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0052_install_group_acl'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexupdate',
            name='to_delete',
            field=models.BooleanField(default=False),
        ),
    ]