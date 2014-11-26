# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('modified_date_time', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
                ('sort_order', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
                ('modified_date_time', models.DateTimeField(auto_now=True)),
                ('is_booked', models.BooleanField(default=True)),
                ('image_slug', models.CharField(max_length=16, null=True, blank=True)),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('sort_order', models.IntegerField(default=0)),
                ('url', models.URLField(null=True, blank=True)),
                ('category', models.ForeignKey(related_name='itm_category_cat', to='wishlist.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
