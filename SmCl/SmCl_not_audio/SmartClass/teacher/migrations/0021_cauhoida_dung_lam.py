# Generated by Django 2.1 on 2018-10-08 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0020_auto_20181005_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='cauhoida',
            name='dung_lam',
            field=models.CharField(default='thi', max_length=255),
            preserve_default=False,
        ),
    ]
