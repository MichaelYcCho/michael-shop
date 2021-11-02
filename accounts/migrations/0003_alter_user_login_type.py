# Generated by Django 3.2.7 on 2021-11-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211021_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login_type',
            field=models.CharField(choices=[('Email', 'Login Email'), ('Kakao', 'Login Kakao')], default='Email', max_length=50),
        ),
    ]
