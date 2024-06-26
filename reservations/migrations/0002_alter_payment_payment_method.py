# Generated by Django 4.2.13 on 2024-05-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('CREDIT_CARD', 'Credit Card'), ('WALLET', 'Wallet'), ('CASH_ON_DELIVERY', 'Cash on Delivery'), ('CAR_POS', 'Car Point of Sale'), ('POINTS', 'Points')], max_length=20),
        ),
    ]
