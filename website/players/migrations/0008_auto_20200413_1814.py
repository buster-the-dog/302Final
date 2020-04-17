# Generated by Django 3.0.4 on 2020-04-13 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_auto_20200413_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defense',
            name='team',
            field=models.ForeignKey(default='pk = 1', on_delete=django.db.models.deletion.CASCADE, to='players.Team'),
        ),
        migrations.AlterField(
            model_name='kicker',
            name='team',
            field=models.ForeignKey(default='pk = 1', on_delete=django.db.models.deletion.CASCADE, to='players.Team'),
        ),
        migrations.AlterField(
            model_name='quarterback',
            name='team',
            field=models.ForeignKey(default='pk = 1', on_delete=django.db.models.deletion.CASCADE, to='players.Team'),
        ),
        migrations.AlterField(
            model_name='runningback',
            name='team',
            field=models.ForeignKey(default='pk = 1', on_delete=django.db.models.deletion.CASCADE, to='players.Team'),
        ),
        migrations.AlterField(
            model_name='tightend',
            name='team',
            field=models.ForeignKey(default='pk = 1', on_delete=django.db.models.deletion.CASCADE, to='players.Team'),
        ),
        migrations.AlterField(
            model_name='widereceiver',
            name='team',
            field=models.ForeignKey(default='pk = 1', on_delete=django.db.models.deletion.CASCADE, to='players.Team'),
        ),
    ]
