# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('create_datetime', models.DateTimeField()),
                ('create_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'uid')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('create_datetime', models.DateTimeField()),
                ('publish_datetime', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
                ('body', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(to='blog.Category', db_column=b'cat_id')),
                ('create_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'uid')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='post_state',
            field=models.ForeignKey(to='blog.State', db_column=b'state_id'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post', db_column=b'post_id'),
            preserve_default=True,
        ),
    ]
