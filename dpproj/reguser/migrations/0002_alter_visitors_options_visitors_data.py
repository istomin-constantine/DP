# Generated by Django 4.0.4 on 2022-05-12 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reguser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitors',
            options={'verbose_name': 'visitors', 'verbose_name_plural': 'visitors'},
        ),
        migrations.AddField(
            model_name='visitors',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
