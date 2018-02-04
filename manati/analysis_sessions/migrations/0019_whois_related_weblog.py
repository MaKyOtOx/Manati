#
# Copyright (c) 2017 Stratosphere Laboratory.
#
# This file is part of ManaTI Project
# (see <https://stratosphereips.org>). It was created by 'Raul B. Netto <raulbeni@gmail.com>'
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. See the file 'docs/LICENSE' or see <http://www.gnu.org/licenses/>
# for copying permission.
#
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-20 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_sessions','0018_analysis_session_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoisRelatedWeblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('weblog_domain_a', models.ForeignKey(db_column='weblog_domain_b', on_delete=django.db.models.deletion.CASCADE, related_name='weblog_domain_b', to='analysis_sessions.Weblog')),
            ],
            options={
                'db_table': 'manati_whois_related_weblogs',
            },
        ),
        migrations.AlterField(
            model_name='webloghistory',
            name='weblog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='analysis_sessions.Weblog'),
        ),
        migrations.AddField(
            model_name='weblog',
            name='whois_related_weblogs',
            field=models.ManyToManyField(related_name='_weblog_whois_related_weblogs_+', through='analysis_sessions.WhoisRelatedWeblog', to='analysis_sessions.Weblog'),
        ),
        migrations.AlterModelOptions(
            name='analysissession',
            options={'permissions': (('read_analysis_session', 'Can read an analysis session'),
                                     ('edit_analysis_session', 'Can edit an analysis session'),
                                     ('create_analysis_session', 'Can create an analysis session'),
                                     ('update_analysis_session', 'Can update an analysis session'))},
        ),
        migrations.AddField(
            model_name='analysissession',
            name='type_file',
            field=models.CharField(
                choices=[('bro_http_log', 'BRO weblogs http.log'), ('cisco_file', 'CISCO weblogs Specific File')],
                max_length=50, null=False, default='cisco_file'),
        ),
    ]