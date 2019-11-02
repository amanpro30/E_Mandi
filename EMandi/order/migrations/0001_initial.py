# Generated by Django 2.2.5 on 2019-11-01 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CropName', models.CharField(max_length=50)),
                ('CropVariety', models.CharField(max_length=50)),
                ('Quantity', models.PositiveIntegerField(default=None)),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('ClosingDate', models.DateTimeField()),
                ('ProductionMode', models.CharField(max_length=50)),
                ('BasePrice', models.FloatField(default=None)),
                ('OrderStatus', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=None)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.MarketOrder')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
