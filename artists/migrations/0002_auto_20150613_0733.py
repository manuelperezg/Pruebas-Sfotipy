# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='fist_name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='artist',
            name='biography',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artist',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
