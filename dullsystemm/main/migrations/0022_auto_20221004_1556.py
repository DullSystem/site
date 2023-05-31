# Generated by Django 3.2.9 on 2022-10-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20220928_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_news',
            name='post_image',
            field=models.ImageField(blank=True, upload_to='gallery', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('lenses', 'lenses'), ('Accessories', 'Accessories'), ('glasses', 'glasses'), ('solutions', 'solutions')], db_index=True, max_length=200, verbose_name='Категория'),
        ),
    ]
