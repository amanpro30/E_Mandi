# Generated by Django 2.2.7 on 2019-12-04 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_avgrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avgrating',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
    ]