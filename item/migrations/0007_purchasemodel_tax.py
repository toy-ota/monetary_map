# Generated by Django 4.0.4 on 2022-05-02 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_alter_purchasedetailmodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasemodel',
            name='tax',
            field=models.FloatField(default='0.1'),
        ),
    ]
