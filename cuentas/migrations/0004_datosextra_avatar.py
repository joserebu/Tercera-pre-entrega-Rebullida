# Generated by Django 4.2.6 on 2023-11-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0003_rename_datosperfil_datosextra'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
