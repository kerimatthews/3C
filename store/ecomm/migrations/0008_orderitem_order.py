# Generated by Django 4.2.2 on 2023-06-29 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0007_rename_products_order_order_num_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='ecomm.order'),
        ),
    ]