# Generated by Django 3.1.1 on 2020-11-28 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profilepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]