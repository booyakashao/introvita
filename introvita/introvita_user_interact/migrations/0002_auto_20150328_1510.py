# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('introvita_user_interact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questions',
            new_name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 8, 58, 913481, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 21, 898012, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicationtojob',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 29, 218547, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicationtojob',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 33, 434275, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authority',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 35, 314438, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authority',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 37, 10366, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidateattributes',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 38, 618598, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidateattributes',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 41, 186704, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 43, 66612, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 46, 346251, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 50, 418746, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 52, 491393, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 54, 314750, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 56, 106871, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 9, 57, 874838, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 10, 0, 618795, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 10, 2, 426938, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 10, 4, 1428, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
