# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-27 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_airavata_wagtail_base', '0014_homepage_show_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cybergatewayhomepage',
            name='show_announcements',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='yes', help_text="Choose yes if you want the Announcements to show up on home page or no if you don't want to", max_length=5),
        ),
    ]
