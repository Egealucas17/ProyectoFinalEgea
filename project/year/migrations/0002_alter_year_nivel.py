# Generated by Django 4.2.6 on 2023-10-17 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nivel', '0001_initial'),
        ('year', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='nivel',
            field=models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.SET_NULL, to='nivel.nivel'),
        ),
    ]
