# Generated by Django 2.1 on 2018-09-13 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_diemso_diem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diemso',
            name='de_id',
        ),
        migrations.AddField(
            model_name='cauhoi',
            name='chu_de',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cauhoi',
            name='dang_cau_hoi',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cauhoi',
            name='do_kho',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diemso',
            name='bai_lam_id',
            field=models.ForeignKey(db_column='bai_lam_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.BaiLamHocSinh'),
        ),
    ]