# Generated by Django 3.2.9 on 2022-11-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20221110_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('glasses', 'glasses'), ('solutions', 'solutions'), ('Accessories', 'Accessories'), ('lenses', 'lenses')], db_index=True, max_length=200, verbose_name='Категория'),
        ),
    ]
