# Generated by Django 5.1.3 on 2024-11-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fecitec', '0004_alter_commission_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionToWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('municipality', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('sub_area', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2)),
                ('formation', models.CharField(choices=[('EnsinoFundamental', 'Ensino Fundamental'), ('EnsinoMedio', 'Ensino Médio')], max_length=20)),
                ('arquivo_modelo', models.FileField(upload_to='uploads/modelos/')),
                ('arquivo_panner', models.FileField(upload_to='uploads/panners/')),
            ],
        ),
    ]
