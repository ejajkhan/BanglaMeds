# Generated by Django 3.2.7 on 2021-11-24 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('description', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Medtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('description', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('description', models.CharField(default='', max_length=1000)),
                ('company', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('disease', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.disease')),
                ('type', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.medtype')),
            ],
        ),
    ]
