# Generated by Django 4.1.2 on 2022-10-15 07:06

from django.db import migrations, models
import file.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to=file.models.upload)),
                ('format', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('ordering', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
