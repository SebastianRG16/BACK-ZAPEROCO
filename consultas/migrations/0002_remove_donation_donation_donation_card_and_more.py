# Generated by Django 4.2.4 on 2023-08-31 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='donation',
        ),
        migrations.AddField(
            model_name='donation',
            name='card',
            field=models.CharField(default=1006857823, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='celphone',
            field=models.CharField(default=3509875689, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='lastName',
            field=models.CharField(default='rodriguez ', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donation',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='donation',
            name='tipe_donation',
            field=models.CharField(choices=[('urna', 'Urna'), ('electrónico', 'Electrónico')], max_length=20),
        ),
    ]
