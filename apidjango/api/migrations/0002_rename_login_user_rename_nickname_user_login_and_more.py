# Generated by Django 4.1 on 2022-08-07 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nickname',
            new_name='login',
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]
