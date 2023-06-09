# Generated by Django 3.2.18 on 2023-04-06 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Menu category',
                'verbose_name_plural': 'Menu categories',
            },
        ),
        migrations.CreateModel(
            name='TreeMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=255, verbose_name='path')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='category')),
                ('parent', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.treemenu', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'Menu item',
                'verbose_name_plural': 'Menu items',
            },
        ),
    ]
