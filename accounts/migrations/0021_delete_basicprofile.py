# Generated by Django 4.0 on 2022-02-09 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_rename_height_no_answer_profile_basics_18_plus_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BasicProfile',
        ),
    ]
