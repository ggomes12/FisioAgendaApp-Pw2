# Generated by Django 5.0.6 on 2024-06-17 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='profissional',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.profissional'),
        ),
    ]