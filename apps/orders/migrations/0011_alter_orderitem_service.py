# Generated by Django 3.2.9 on 2021-12-25 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_alter_reviewrating_review'),
        ('orders', '0010_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.serviceoption'),
        ),
    ]