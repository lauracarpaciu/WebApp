# Generated by Django 4.0 on 2022-02-25 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='created_by',
            new_name='author',
        ),
    ]
