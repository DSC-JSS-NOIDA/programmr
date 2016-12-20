# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('detail', models.TextField()),
                ('constraint', models.CharField(max_length=120)),
                ('input_format', models.TextField()),
                ('output_format', models.TextField()),
                ('sample_testcase', models.TextField()),
                ('testcase_input', models.TextField()),
                ('testcase_output', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.CharField(max_length=120)),
                ('question_ID', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=120)),
                ('source_code_URL', models.URLField(max_length=120)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email_ID', models.CharField(max_length=200)),
                ('avatar', models.URLField(max_length=120)),
                ('year', models.CharField(max_length=120)),
                ('branch', models.CharField(max_length=120)),
                ('mobile_no', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('total_score', models.CharField(max_length=120)),
            ],
        ),
    ]
