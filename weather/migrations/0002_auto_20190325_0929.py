# Generated by Django 2.1.7 on 2019-03-25 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
        migrations.RenameField(
            model_name='city',
            old_name='city',
            new_name='city_name',
        ),
    ]