# Generated by Django 5.0 on 2023-12-31 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoesapp', '0005_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('QueryID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('Telephone', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('Email', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('Address', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('Image', models.ImageField(null=True, upload_to='media/product')),
                ('Message', models.TextField(verbose_name='Your Message')),
            ],
        ),
    ]
