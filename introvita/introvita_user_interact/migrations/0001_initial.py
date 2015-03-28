# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApplicationToJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('applied', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CandidateAttributes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passionsAndGoals', models.CharField(max_length=500)),
                ('workProjectDone', models.TextField()),
                ('skills', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('summary', models.TextField()),
                ('qualifications', models.TextField()),
                ('responsibilities', models.TextField()),
                ('salary', models.CharField(max_length=150)),
                ('limit', models.IntegerField()),
                ('applied', models.IntegerField()),
                ('enabled', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questions', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=100)),
                ('middleName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=100)),
                ('addressLine1', models.CharField(max_length=300)),
                ('addressLine2', models.CharField(max_length=300)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('emailAddress', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('zipcode', models.IntegerField()),
                ('paymentId', models.CharField(max_length=500)),
                ('company', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=200)),
                ('positionAtCompany', models.CharField(max_length=150)),
                ('authority', models.ForeignKey(to='introvita_user_interact.Authority')),
                ('state', models.ForeignKey(to='introvita_user_interact.State')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='questionsId',
            field=models.ForeignKey(to='introvita_user_interact.Questions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='employer',
            field=models.ForeignKey(to='introvita_user_interact.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='questionsId',
            field=models.ForeignKey(to='introvita_user_interact.Questions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidateattributes',
            name='user',
            field=models.ForeignKey(to='introvita_user_interact.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicationtojob',
            name='candidate',
            field=models.ForeignKey(to='introvita_user_interact.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicationtojob',
            name='jobPost',
            field=models.ForeignKey(to='introvita_user_interact.JobPost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='candidate',
            field=models.ForeignKey(to='introvita_user_interact.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='questions',
            field=models.ForeignKey(to='introvita_user_interact.Question'),
            preserve_default=True,
        ),
    ]
