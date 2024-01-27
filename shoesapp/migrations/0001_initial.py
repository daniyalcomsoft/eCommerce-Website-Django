# Generated by Django 5.0 on 2023-12-27 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('BrandID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255, verbose_name='Brand Name')),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('ConditionID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255, verbose_name='Shoes Condition')),
                ('Image', models.ImageField(null=True, upload_to='media/product')),
            ],
        ),
        migrations.CreateModel(
            name='ShoesReviews',
            fields=[
                ('ShoesReviewsID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255, verbose_name='Shoes Condition')),
                ('Image', models.ImageField(null=True, upload_to='media/product')),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('SizeID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255, verbose_name='Shoes Size')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('TypeID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255, verbose_name='Shoes Type')),
            ],
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('ShoesID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255, verbose_name='Shoes Name')),
                ('CutPrice', models.CharField(max_length=255, verbose_name='Cut Price')),
                ('Price', models.CharField(max_length=255, verbose_name='Actual Price')),
                ('Image', models.ImageField(null=True, upload_to='media/product')),
                ('Description', models.TextField(verbose_name='Description')),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shoesapp.brand', verbose_name='Shoes Brand')),
                ('Condition', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shoesapp.condition', verbose_name='Shoes Condition')),
                ('Size', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shoesapp.size', verbose_name='Shoes Size')),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shoesapp.type', verbose_name='Shoes Type')),
            ],
        ),
        migrations.CreateModel(
            name='ShoesImage',
            fields=[
                ('PID', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(null=True, upload_to='media/product')),
                ('Shoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoesapp.shoes', verbose_name='Shoes Name')),
            ],
        ),
    ]
