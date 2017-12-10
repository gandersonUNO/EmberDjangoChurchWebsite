# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-08 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171203_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('document', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.DeleteModel(
            name='ApiKey',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
