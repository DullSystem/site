# Generated by Django 3.2.9 on 2022-11-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20221109_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default=1, upload_to='gallery', verbose_name='Развёрнутый вид товара'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Accessories', 'Accessories'), ('lenses', 'lenses'), ('solutions', 'solutions'), ('glasses', 'glasses')], db_index=True, max_length=200, verbose_name='Категория'),
        ),
    ]