# Generated by Django 5.1.2 on 2024-12-06 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_participante_instituicao_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participante',
            old_name='municipio',
            new_name='municipio_participante',
        ),
    ]
