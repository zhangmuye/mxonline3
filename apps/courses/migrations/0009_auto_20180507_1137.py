# Generated by Django 2.0.1 on 2018-05-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20180506_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.FileField(max_length=500, upload_to='medi/video/%Y/%m', verbose_name='资源文件'),
        ),
    ]
