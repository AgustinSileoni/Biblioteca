# Generated by Django 4.0.1 on 2022-05-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('nacionalidad', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]