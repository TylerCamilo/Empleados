# Generated by Django 5.0.2 on 2024-03-28 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_habilidades_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.habilidades'),
        ),
    ]
