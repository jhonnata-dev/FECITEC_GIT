
# Generated by Django 5.1.2 on 2024-11-01 11:26

import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('formation', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='', variations={})),
            ],
        ),
    ]
