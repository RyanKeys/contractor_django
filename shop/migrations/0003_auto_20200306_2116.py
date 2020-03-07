# Generated by Django 2.2.6 on 2020-03-06 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_auto_20200306_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of your listing:', max_length=50)),
                ('slug', models.CharField(blank=True, editable=False, help_text='Unique URL path to access this page. Generated by the system.', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time model was created')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
