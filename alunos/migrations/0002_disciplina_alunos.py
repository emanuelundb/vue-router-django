# Generated by Django 3.1.4 on 2020-12-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='alunos',
            field=models.ManyToManyField(related_name='disciplinas', to='alunos.Aluno'),
        ),
    ]