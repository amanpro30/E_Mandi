# Generated by Django 2.2.5 on 2019-10-18 20:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=100)),
                ('phone', models.IntegerField(max_length=10, validators=[django.core.validators.RegexValidator('\\d{10,10}')])),
                ('image', models.ImageField(blank=True, upload_to='image_profile')),
                ('state', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=500)),
                ('aadharcard', models.BigIntegerField(default=0)),
                ('pincode', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
