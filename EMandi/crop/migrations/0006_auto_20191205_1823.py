# Generated by Django 2.2.7 on 2019-12-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0005_auto_20191205_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
