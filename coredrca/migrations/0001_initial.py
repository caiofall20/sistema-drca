# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('matricula', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('d_credito', models.IntegerField()),
                ('d_credito_p', models.IntegerField()),
                ('a_credito_o', models.IntegerField()),
                ('a_credito_l', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=30)),
                ('obr_let', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('credito', models.ForeignKey(to='coredrca.Credito')),
                ('curso', models.ForeignKey(to='coredrca.Curso')),
                ('d_requisito', models.ManyToManyField(to='coredrca.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('departamento', models.ForeignKey(to='coredrca.Departamento', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=30)),
                ('tipo', models.IntegerField()),
                ('departamento', models.ForeignKey(to='coredrca.Departamento', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(to='coredrca.Professor', null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='secretaria',
            field=models.ForeignKey(to='coredrca.Secretaria', null=True),
        ),
        migrations.AddField(
            model_name='aluno',
            name='credito',
            field=models.ForeignKey(to='coredrca.Credito'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(to='coredrca.Curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='diciplinas',
            field=models.ManyToManyField(to='coredrca.Disciplina'),
        ),
    ]
