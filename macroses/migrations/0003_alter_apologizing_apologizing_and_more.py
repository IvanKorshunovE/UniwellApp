# Generated by Django 4.1.7 on 2023-03-15 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macroses', '0002_apologizing_askingthereason_ending_tail_thanking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apologizing',
            name='apologizing',
            field=models.TextField(max_length=3000, verbose_name='Apologizing'),
        ),
        migrations.AlterField(
            model_name='askingthereason',
            name='ask_reason',
            field=models.TextField(max_length=3000, verbose_name='AskingTheReason'),
        ),
        migrations.AlterField(
            model_name='ending',
            name='ending',
            field=models.TextField(max_length=1100, verbose_name='Ending'),
        ),
        migrations.AlterField(
            model_name='greeting',
            name='greeting',
            field=models.TextField(max_length=120, verbose_name='Greeting'),
        ),
        migrations.AlterField(
            model_name='tail',
            name='tail',
            field=models.TextField(max_length=120, verbose_name='The most end part'),
        ),
        migrations.AlterField(
            model_name='thanking',
            name='thanking',
            field=models.TextField(max_length=120, verbose_name='Thanking'),
        ),
    ]
