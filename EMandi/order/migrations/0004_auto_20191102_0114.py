# Generated by Django 2.2.5 on 2019-11-01 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0003_auto_20191102_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='userid',
        ),
        migrations.CreateModel(
            name='Bidmid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Bid')),
                ('userid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
