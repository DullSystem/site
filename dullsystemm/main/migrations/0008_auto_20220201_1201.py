# Generated by Django 3.2.9 on 2022-02-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220125_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категория товаров', 'verbose_name_plural': 'Категории товаров'},
        ),
        migrations.AlterModelOptions(
            name='prices',
            options={'verbose_name': 'Наименование услуги (врача)', 'verbose_name_plural': 'Наименование услуг (врача)'},
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Плановая замена'),
        ),
    ]
