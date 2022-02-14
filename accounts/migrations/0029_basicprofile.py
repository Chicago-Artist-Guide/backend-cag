# Generated by Django 4.0 on 2022-02-10 04:58

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_delete_basicprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pronouns', models.CharField(max_length=255)),
                ('lgbtqia', models.CharField(max_length=255)),
                ('ethnicities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('height_feet', models.IntegerField(blank=True, null=True)),
                ('height_inches', models.IntegerField(blank=True, null=True)),
                ('height_no_answer', models.BooleanField(default=False)),
                ('age_range', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('gender_roles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('gender_transition', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('offstage_general', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('offstage_production', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('offstage_scenic_and_properties', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('offstage_lighting', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('offstage_sound', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('offstage_hair_makeup_costumes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('profile_image_url', models.TextField(blank=True, null=True)),
                ('union_status', models.CharField(max_length=255)),
                ('agency', models.CharField(max_length=255)),
                ('websites', models.JSONField()),
                ('bio', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
