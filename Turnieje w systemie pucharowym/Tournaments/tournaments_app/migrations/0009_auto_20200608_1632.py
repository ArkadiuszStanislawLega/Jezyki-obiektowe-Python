# Generated by Django 3.0.7 on 2020-06-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments_app', '0008_remove_team_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='score_a',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='score_b',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
