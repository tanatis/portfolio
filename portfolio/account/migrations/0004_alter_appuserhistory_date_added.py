# Generated by Django 4.2.4 on 2023-09-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_user_appuserhistory_to_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuserhistory',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
