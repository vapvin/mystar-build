# Generated by Django 2.2.5 on 2021-10-28 08:37

from django.db import migrations, models
import pictures.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_auto_20211028_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picturemodel',
            name='image',
            field=models.ImageField(height_field='height', upload_to='photos/%y/%m/%d', validators=[pictures.validators.validate_file_size], width_field='width'),
        ),
    ]
