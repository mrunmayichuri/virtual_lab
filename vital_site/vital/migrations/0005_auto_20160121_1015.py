# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vital', '0004_auto_20160120_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('backing_file', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Network_Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('virtual_machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital.Virtual_Machines')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='students_registered',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='type',
            field=models.CharField(choices=[('PR', 'Professor'), ('TA', 'TeachingAssistant'), ('OW', 'Owner')], default='PR', max_length=2),
        ),
        migrations.AddField(
            model_name='virtual_machines',
            name='base_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vital.Base_Image'),
        ),
    ]
