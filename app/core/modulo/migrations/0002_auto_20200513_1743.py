# Generated by Django 2.2.12 on 2020-05-13 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_auto_20200513_1514'),
        ('modulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categproye',
            options={'verbose_name': 'Categoría del Proyecto', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='tipodocu',
            options={'verbose_name': 'Tipo de Documento', 'verbose_name_plural': 'Tipos de Documentos'},
        ),
        migrations.RemoveField(
            model_name='categproye',
            name='Lenguaje',
        ),
        migrations.AddField(
            model_name='categproye',
            name='arquitectura',
            field=models.CharField(max_length=300, null=True, verbose_name='Arquitectura del Proyecto'),
        ),
        migrations.AddField(
            model_name='categproye',
            name='lenguaje',
            field=models.CharField(max_length=50, null=True, verbose_name='Lenguaje del Proyecto'),
        ),
        migrations.AddField(
            model_name='categproye',
            name='motorDB',
            field=models.CharField(max_length=200, null=True, verbose_name='Base de Datos utilizada para el proyecto'),
        ),
        migrations.AlterField(
            model_name='tipodocu',
            name='NombTiDoc',
            field=models.CharField(max_length=50, verbose_name='Nombre Tipo de Documento'),
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de inicio')),
                ('fechaFin', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de fin')),
                ('nombProyecto', models.CharField(max_length=100, verbose_name='Nombre del Proyecto')),
                ('estaProyecto', models.CharField(max_length=100, verbose_name='Estado del Proyecto')),
                ('urlRepo', models.TextField(verbose_name='Url de repositorio')),
                ('descProyecto', models.TextField(verbose_name='Descripción del Proyecto')),
                ('imgProyecto', models.ImageField(default='proyecto.png', null=True, upload_to='', verbose_name='Imagen del Proyecto')),
                ('idCategProye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo.CategProye', verbose_name='Identificador de Categoría')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombDocu', models.CharField(max_length=100, verbose_name='Nombre de Documento')),
                ('pathDocu', models.CharField(max_length=100, verbose_name='Ruta de Almacenamiento')),
                ('idProyectos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo.Proyectos', verbose_name='Identificación dl proyecto')),
                ('idTipoDocu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo.TipoDocu', verbose_name='Identificación de Tipo de Documento')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DatosUser', verbose_name='Identificación de usuario')),
            ],
            options={
                'verbose_name': 'Documento del Proyecto',
                'verbose_name_plural': 'Documentos del Proyecto',
            },
        ),
    ]
