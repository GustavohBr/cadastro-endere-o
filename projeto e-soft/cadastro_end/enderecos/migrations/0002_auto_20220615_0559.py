# Generated by Django 3.2.5 on 2022-06-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enderecos',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='enderecos',
            name='descriçao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
