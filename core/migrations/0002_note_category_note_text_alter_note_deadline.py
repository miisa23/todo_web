# Generated by Django 4.2.13 on 2024-06-01 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='note',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='note',
            name='deadline',
            field=models.CharField(max_length=15, verbose_name='Срок выполнения задачи'),
        ),
    ]