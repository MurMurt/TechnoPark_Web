# Generated by Django 2.0.3 on 2018-04-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180422_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='static/user_avatars/User_Avatar.png', upload_to='static/user_avatars'),
        ),
    ]
