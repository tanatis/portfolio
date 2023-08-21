# Generated by Django 4.2.4 on 2023-08-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0005_alter_positionhistory_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='positionhistory',
            name='count',
        ),
        migrations.RemoveField(
            model_name='positionhistory',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='positionhistory',
            name='price',
        ),
        migrations.AddField(
            model_name='positionhistory',
            name='info',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
