# Generated by Django 2.2.6 on 2019-11-04 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20191104_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketorder',
            old_name='Created_by',
            new_name='user',
        ),
    ]