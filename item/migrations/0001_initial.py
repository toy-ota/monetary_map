# Generated by Django 4.0.4 on 2022-04-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
