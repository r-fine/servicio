# Generated by Django 3.2.9 on 2021-12-04 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20211204_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail Address'),
        ),
        migrations.AlterField(
            model_name='localuser',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
