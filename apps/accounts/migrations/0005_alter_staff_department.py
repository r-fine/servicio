# Generated by Django 3.2.9 on 2021-12-21 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20211221_1827'),
        ('accounts', '0004_alter_localuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='services.service'),
            preserve_default=False,
        ),
    ]