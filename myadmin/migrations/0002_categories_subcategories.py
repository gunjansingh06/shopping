# Generated by Django 5.0.6 on 2024-07-04 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat_name', models.CharField(max_length=100)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.categories')),
            ],
            options={
                'db_table': 'subcategories',
            },
        ),
    ]
