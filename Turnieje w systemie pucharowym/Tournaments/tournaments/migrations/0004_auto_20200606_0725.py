# Generated by Django 2.2.8 on 2020-06-06 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_player'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('is_win', models.BooleanField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tournaments.Game')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tournaments.Team')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='score_a',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='game_core_a_team', to='tournaments.Score'),
        ),
        migrations.AddField(
            model_name='game',
            name='score_b',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='game_score_b_team', to='tournaments.Score'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='game_a_team', to='tournaments.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='game_b_team', to='tournaments.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament'),
        ),
    ]
