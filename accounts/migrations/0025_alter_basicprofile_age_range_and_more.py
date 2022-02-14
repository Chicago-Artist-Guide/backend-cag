# Generated by Django 4.0 on 2022-02-10 04:55

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_basicprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicprofile',
            name='age_range',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='agency',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='bio',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='ethnicities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='gender',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='gender_roles',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='gender_transition',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='lgbtqia',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='offstage_general',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='offstage_hair_makeup_costumes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='offstage_lighting',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='offstage_production',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='offstage_scenic_and_properties',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='offstage_sound',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='profile_image_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='pronouns',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='union_status',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
        ),
    ]