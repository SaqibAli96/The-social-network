# Generated by Django 3.1.1 on 2020-12-01 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profilepage', '0006_auto_20201201_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentbox',
            name='comment',
            field=models.TextField(max_length=250),
        ),
    ]