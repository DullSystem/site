# Generated by Django 3.2.9 on 2022-02-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220201_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='optical',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Оптическая сила'),
        ),
        migrations.AlterField(
            model_name='product',
            name='radius',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=10, verbose_name='Радиус кривизны'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, db_index=True, max_length=200, verbose_name='Плановая замена'),
        ),
    ]
