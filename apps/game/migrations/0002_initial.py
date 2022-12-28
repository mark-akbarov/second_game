# Generated by Django 4.1.2 on 2022-11-16 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        # ('file', '0001_initial'),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='collection',
            field=models.ManyToManyField(blank=True, to='game.collection'),
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file.file'),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('collection', 'item')},
        ),
    ]
