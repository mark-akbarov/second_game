# Generated by Django 4.1.2 on 2022-10-22 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_item_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='collection',
        ),
        migrations.AddField(
            model_name='item',
            name='collection',
            field=models.ManyToManyField(to='game.collection'),
        ),
    ]