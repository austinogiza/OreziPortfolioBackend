# Generated by Django 3.1.2 on 2021-01-10 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0002_contact_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('brief', models.TextField()),
                ('challenges', models.TextField()),
                ('approach', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('image1', models.URLField(blank=True, null=True)),
                ('image2', models.URLField(blank=True, null=True)),
                ('image3', models.URLField(blank=True, null=True)),
                ('image4', models.URLField(blank=True, null=True)),
                ('image5', models.URLField(blank=True, null=True)),
                ('image6', models.URLField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('post', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
