# Generated by Django 2.2.5 on 2021-10-26 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20211021_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='save_pass',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
