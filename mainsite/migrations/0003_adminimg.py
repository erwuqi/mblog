# Generated by Django 2.0.1 on 2018-02-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20180113_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminIMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(upload_to='./admin')),
            ],
        ),
    ]
