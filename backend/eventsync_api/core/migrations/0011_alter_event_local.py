# Generated by Django 5.0.4 on 2024-08-22 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_registrationpresence_presence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.local'),
        ),
    ]