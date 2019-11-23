# Generated by Django 2.2.6 on 2019-11-23 12:19

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('venue_website', models.URLField(default='', max_length=100)),
                ('venue_photo', models.ImageField(blank=True, upload_to='venue_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(verbose_name='start time and date')),
                ('end_time', models.DateTimeField(verbose_name='end time and date')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, upload_to='event_photos')),
                ('attendees', models.ManyToManyField(default='', related_name='attendees', to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(default='', to='eventfinder.Category')),
                ('host', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='eventfinder.Venue')),
            ],
        ),
    ]
