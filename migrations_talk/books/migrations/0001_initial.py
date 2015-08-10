# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_first_name', models.CharField(max_length=50)),
                ('author_last_name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('number_pages', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
