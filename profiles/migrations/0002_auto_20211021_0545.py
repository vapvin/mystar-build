# Generated by Django 2.2.5 on 2021-10-21 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='company',
            field=models.CharField(blank=True, default='Free', max_length=50, null=True),
        ),
    ]