# Generated by Django 3.2.16 on 2022-10-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('AGUARDANDO', 'Aguardando autorização'), ('EM_VISITA', 'Em visita'), ('FINALIZADO', 'visita finalizada')], default='AGUARDANDO', max_length=10, verbose_name='Status')),
                ('nome_completo', models.CharField(max_length=194, verbose_name='Nome completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
                ('numero_casa', models.PositiveSmallIntegerField(verbose_name='Número da casa a ser visitada')),
                ('placa_veiculo', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa do veículo')),
                ('horario_chegada', models.DateTimeField(auto_now_add=True, verbose_name='Horário de chegada na portaria')),
                ('horario_saida', models.DateTimeField(blank=True, null=True, verbose_name='Horário de saída do condomínio')),
                ('horario_autorizacao', models.DateTimeField(blank=True, null=True, verbose_name='Horário de autorização de entrada')),
                ('morador_responsavel', models.CharField(blank=True, max_length=194, verbose_name='Nome do morador de autorizar a entrada do visitante')),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitantes',
                'db_table': 'visitante',
            },
        ),
    ]
