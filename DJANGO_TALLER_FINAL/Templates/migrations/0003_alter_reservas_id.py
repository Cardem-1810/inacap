# Generated by Django 4.1 on 2022-12-21 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Templates', '0002_rename_persona_reservas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]