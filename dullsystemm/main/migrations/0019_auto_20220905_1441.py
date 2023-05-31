# Generated by Django 3.2.9 on 2022-09-05 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0018_auto_20220904_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments_user',
            options={'ordering': ['created_on'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AddField(
            model_name='comments_user',
            name='author_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments_user',
            name='body',
            field=models.TextField(verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='comments_user',
            name='username',
            field=models.CharField(blank=True, max_length=80, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Accessories', 'Accessories'), ('glasses', 'glasses'), ('lenses', 'lenses'), ('solutions', 'solutions')], db_index=True, max_length=200, verbose_name='Категория'),
        ),
    ]