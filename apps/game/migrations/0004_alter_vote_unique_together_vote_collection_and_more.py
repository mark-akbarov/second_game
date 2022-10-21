# Generated by Django 4.1.2 on 2022-10-19 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_item_options_item_votes'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='vote',
            name='collection',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='game.collection'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='vote',
            name='item',
        ),
    ]
