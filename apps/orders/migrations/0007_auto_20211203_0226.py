# Generated by Django 3.2.9 on 2021-12-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20211203_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(verbose_name='Delivery Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.TimeField(verbose_name='Delivery Time'),
        ),
    ]