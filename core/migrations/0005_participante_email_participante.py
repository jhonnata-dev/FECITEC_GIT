# Generated by Django 5.1.2 on 2024-12-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_participante_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='email_participante',
            field=models.EmailField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]