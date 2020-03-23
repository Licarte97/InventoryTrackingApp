# Generated by Django 3.0.4 on 2020-03-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodType', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('field1', models.CharField(max_length=255)),
                ('field1_lbl', models.CharField(blank=True, max_length=3)),
                ('field2', models.CharField(blank=True, max_length=255)),
                ('field2_lbl', models.CharField(blank=True, max_length=3)),
                ('field3', models.CharField(blank=True, max_length=255)),
                ('field3_lbl', models.CharField(blank=True, max_length=3)),
                ('stock', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodType', models.CharField(max_length=255)),
                ('field1_name', models.CharField(max_length=255)),
                ('field2_name', models.CharField(max_length=255)),
                ('field3_name', models.CharField(max_length=255)),
            ],
        ),
    ]
