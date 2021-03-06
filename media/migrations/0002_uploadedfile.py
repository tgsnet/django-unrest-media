# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-02 18:25
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import lablackey.db.models
import lablackey.unrest


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.FileField(blank=True, max_length=200, null=True, storage=django.core.files.storage.FileSystemStorage(base_url=b'/private_file/', location=b'/home/chriscauley/thegamesupply/main/../.media'), upload_to=b'%Y%m')),
                ('name', models.CharField(max_length=256)),
                ('content_type', models.CharField(max_length=256)),
            ],
            bases=(models.Model, lablackey.db.models.UserOrSessionMixin, lablackey.unrest.JsonMixin),
        ),
    ]
