# Generated by Django 4.0.4 on 2022-05-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipField', models.CharField(max_length=45, verbose_name='IP')),
                ('protocolField', models.CharField(max_length=4, verbose_name='protocol')),
                ('countryField', models.CharField(max_length=50, verbose_name='country')),
                ('cityField', models.CharField(max_length=50, verbose_name='city')),
                ('providerField', models.TextField(verbose_name='provider')),
            ],
        ),
    ]
