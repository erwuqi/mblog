# Generated by Django 2.0.1 on 2018-02-03 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_delete_adminimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='kind',
            field=models.CharField(choices=[('1', '科技'), ('2', '时事'), ('3', '旅行'), ('4', '生活'), ('5', '资讯'), ('6', '文学'), ('7', '感情')], default=('1', '科技'), max_length=20, verbose_name='分类'),
        ),
    ]
