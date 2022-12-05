# Generated by Django 3.2.12 on 2022-12-04 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AdminPanel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicule',
            name='nombre_place',
        ),
        migrations.AddField(
            model_name='vehicule',
            name='type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='capacite',
            field=models.IntegerField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='destination',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.destination'),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='immatriculation',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='nom_vehicule',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='trajet',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.trajet'),
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]