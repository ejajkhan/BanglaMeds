# Generated by Django 3.2.7 on 2021-11-23 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuperCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superCategory_name', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='', max_length=30)),
                ('superCategory_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.supercategory')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(default='', max_length=50)),
                ('car_driverRate', models.IntegerField(default=0)),
                ('car_hourRate', models.IntegerField(default=0)),
                ('car_deliveryRate', models.IntegerField(default=0)),
                ('car_capacity', models.IntegerField(default=0)),
                ('car_quantity', models.IntegerField(default=0)),
                ('car_image', models.ImageField(default='', upload_to='shop/images')),
                ('car_category', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.category')),
            ],
        ),
    ]