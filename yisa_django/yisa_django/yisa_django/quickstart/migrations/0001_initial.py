# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chengjiu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chengjiuID', models.TextField()),
                ('chengjiuUrl', models.TextField()),
                ('chineseName', models.TextField()),
                ('englishName', models.TextField()),
                ('imageName', models.TextField()),
                ('imageUrl', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Daoju',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('englishName', models.TextField()),
                ('daojuUrl', models.TextField()),
                ('chineseName', models.TextField()),
                ('imageName', models.TextField()),
                ('imageUrl', models.TextField()),
                ('daojuID', models.TextField()),
                ('daojuChongneng', models.TextField()),
                ('daojuXiaoguo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shipinUrl', models.TextField()),
                ('chineseName', models.TextField()),
                ('imageName', models.TextField()),
                ('imageUrl', models.TextField()),
                ('shipinID', models.TextField()),
                ('shipinXiaoguo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Wupin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('wupinUrl', models.TextField()),
                ('chineseName', models.TextField()),
                ('imageName', models.TextField()),
                ('imageUrl', models.TextField()),
                ('wupinID', models.TextField()),
                ('wupinXiaoguo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Yaowan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('englishName', models.TextField()),
                ('yaowanUrl', models.TextField()),
                ('chineseName', models.TextField()),
                ('yaowanID', models.TextField()),
                ('yaowanXiaoguo', models.TextField()),
            ],
        ),
    ]
