# Generated by Django 3.2.5 on 2021-11-18 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_alter_user_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('aplicacion.user',),
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('LUNES', 'LUNES'), ('MARTES', 'MARTES'), ('MIERCOLES', 'MIERCOLES'), ('JUEVES', 'JUEVES'), ('VIERNES', 'VIERNES')], max_length=20)),
                ('hora', models.CharField(choices=[('8:00', '8:00'), ('8:30', '8:30'), ('9:00', '9:00'), ('9:30', '9:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30')], max_length=20)),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agente_turno', to='aplicacion.agente')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_turno', to='aplicacion.cliente')),
            ],
        ),
    ]