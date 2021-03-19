# Generated by Django 3.1.7 on 2021-03-19 08:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogsapp', '0002_auto_20210319_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='breed',
            old_name='lifespan',
            new_name='size',
        ),
        migrations.RemoveField(
            model_name='breed',
            name='temperment',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='created',
        ),
        migrations.AddField(
            model_name='breed',
            name='exerciseneeds',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breed',
            name='friendliness',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breed',
            name='sheddingamount',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breed',
            name='trainability',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dog',
            name='color',
            field=models.CharField(default='grey', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dog',
            name='favoritefood',
            field=models.CharField(default='meat', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dog',
            name='favoritetoy',
            field=models.CharField(default='ball', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dog',
            name='gender',
            field=models.CharField(default='male', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dog',
            name='age',
            field=models.IntegerField(),
        ),
    ]
