# Generated by Django 4.0 on 2022-02-10 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_alter_basicprofile_age_range_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BasicProfile',
        ),
    ]