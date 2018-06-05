# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 07:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('misago_threads', '0015_report_record_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invited_email', models.CharField(max_length=64)),
                ('created_on', models.DateTimeField(db_index=True)),
                ('updated_on', models.DateTimeField()),
                ('invitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='userinvitation',
            index=models.Index(fields=['invited_email'], name='misago_thre_invited_a982ed_idx'),
        ),
    ]