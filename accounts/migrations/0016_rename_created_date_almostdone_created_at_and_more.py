# Generated by Django 4.0 on 2022-01-28 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_almostdone_union'),
    ]

    operations = [
        migrations.RenameField(
            model_name='almostdone',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='almostdone',
            old_name='date_modified',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='date_modified',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='getsomedetails',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='getsomedetails',
            old_name='date_modified',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='date_modified',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='whatdoyoulikedoing',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='whatdoyoulikedoing',
            old_name='date_modified',
            new_name='updated_at',
        ),
    ]
