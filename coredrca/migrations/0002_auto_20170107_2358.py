# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coredrca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='diciplinas',
            field=models.ManyToManyField(to='coredrca.Disciplina', blank=True),
        ),
    ]
