# Generated by Django 4.0 on 2022-02-10 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_basicprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
