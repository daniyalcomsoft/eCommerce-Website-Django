# Generated by Django 5.0 on 2023-12-31 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoesapp', '0004_gallery_alter_shoesreviews_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('ContactID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('Telephone', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('Email', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('Address', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('Message', models.TextField(verbose_name='Your Message')),
            ],
        ),
    ]
