# Generated by Django 2.0.1 on 2018-01-13 05:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='kind',
            field=models.CharField(choices=[('1', '科技'), ('2', '国内'), ('3', '国外'), ('4', '生活'), ('5', '资讯')], default=('1', '科技'), max_length=20, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=200, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='标题'),
        ),
    ]
