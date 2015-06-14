# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
        ('artists', '0002_auto_20150613_0733'),
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='album',
            field=models.ForeignKey(default=None, to='albums.Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='artis',
            field=models.ForeignKey(default=None, to='artists.Artist'),
            preserve_default=False,
        ),
    ]
