# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0003_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
