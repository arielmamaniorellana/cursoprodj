# Generated by Django 3.2.5 on 2021-07-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0004_auto_20210719_1649'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidad Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['-first_name', 'last_name'], 'verbose_name': 'Mi Empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO')], max_length=1, verbose_name='Trabajo'),
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('first_name', 'departamento')},
        ),
    ]
