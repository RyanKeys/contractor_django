# Generated by Django 3.0.4 on 2020-03-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200307_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='picture',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
