# Generated by Django 4.0 on 2022-02-09 13:28

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_rename_basics_18_plus_profile_height_no_answer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='height_no_answer',
            new_name='basics_18_plus',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='age_range',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='agency',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ethnicities',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender_roles',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender_transition',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='height_feet',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='height_inches',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lgbtqia',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='offstage_general',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='offstage_hair_makeup_costumes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='offstage_lighting',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='offstage_production',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='offstage_scenic_and_properties',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='offstage_sound',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_image_url',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pronouns',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='union_status',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='websites',
        ),
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.CharField(choices=[('individual_artist', 'Individual Artist'), ('theatre_group', 'Theatre Group')], default='individual_artist', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='perform',
            field=models.CharField(choices=[('on_stage', 'On Stage'), ('off_stage', 'Off Stage'), ('both', 'Both')], default='on_stage', max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='privacy_agreement',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile-images/'),
        ),
        migrations.CreateModel(
            name='BasicProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pronouns', models.CharField(blank=True, max_length=255, null=True)),
                ('lgbtqia', models.CharField(blank=True, max_length=255, null=True)),
                ('ethnicities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('height_feet', models.IntegerField(blank=True, null=True)),
                ('height_inches', models.IntegerField(blank=True, null=True)),
                ('height_no_answer', models.BooleanField(default=False)),
                ('age_range', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('gender_roles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('gender_transition', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('offstage_general', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('offstage_production', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('offstage_scenic_and_properties', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('offstage_lighting', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('offstage_sound', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('offstage_hair_makeup_costumes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('profile_image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('union_status', models.CharField(blank=True, max_length=255, null=True)),
                ('agency', models.CharField(blank=True, max_length=255, null=True)),
                ('websites', models.JSONField()),
                ('bio', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
