# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-02 07:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_image', models.ImageField(upload_to='')),
                ('scores', jsonfield.fields.JSONField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face.Image')),
            ],
        ),
    ]
