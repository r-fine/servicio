# Generated by Django 3.2.9 on 2021-12-24 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_orderitem_order'),
        ('accounts', '0012_alter_staffbookeddatetime_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffbookeddatetime',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.orderitem'),
        ),
    ]