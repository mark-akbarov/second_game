# Generated by Django 4.1.2 on 2022-11-19 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_vote_unique_together_remove_vote_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='collection',
        ),
    ]