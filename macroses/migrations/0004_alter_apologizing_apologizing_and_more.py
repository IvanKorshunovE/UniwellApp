# Generated by Django 4.1.7 on 2023-03-15 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macroses', '0003_alter_apologizing_apologizing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apologizing',
            name='apologizing',
            field=models.TextField(max_length=4000, verbose_name='Apologizing'),
        ),
        migrations.AlterField(
            model_name='askingthereason',
            name='ask_reason',
            field=models.TextField(max_length=4000, verbose_name='AskingTheReason'),
        ),
        migrations.AlterField(
            model_name='ending',
            name='ending',
            field=models.TextField(max_length=2100, verbose_name='Ending'),
        ),
        migrations.AlterField(
            model_name='thanking',
            name='thanking',
            field=models.TextField(max_length=2000, verbose_name='Thanking'),
        ),
    ]
