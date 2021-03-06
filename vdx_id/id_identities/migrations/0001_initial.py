# Generated by Django 2.2.10 on 2020-11-23 15:02

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VdxIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('properties', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('unique_identifier', models.CharField(max_length=80, unique=True, verbose_name='Unique identifier for this identity')),
                ('access_synchronized', models.BooleanField(default=True)),
            ],
            options={
                'permissions': (('identity_admin', 'User can alter all VdxIdentity objects'),),
            },
        ),
    ]
