# Generated by Django 4.1.7 on 2023-03-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macroses', '0009_gowith'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotUserFriendly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('not_user_friendly', models.TextField(max_length=5000, verbose_name='Not User Friendly/ Difficult to use')),
            ],
        ),
    ]
