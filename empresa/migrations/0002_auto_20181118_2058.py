# Generated by Django 2.1.3 on 2018-11-18 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(blank=True, help_text='Nome da empresa', max_length=100, null=True),
        ),
    ]
