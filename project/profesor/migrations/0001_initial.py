# Generated by Django 4.2.6 on 2023-10-17 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=30)),
                ('contacto', models.EmailField(max_length=254)),
            ],
        ),
    ]