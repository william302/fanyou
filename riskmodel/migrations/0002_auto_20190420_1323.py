# Generated by Django 2.1.2 on 2019-04-20 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='greylistdetail',
            name='type',
            field=models.CharField(max_length=80, null=True, verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='platformdetail',
            name='type',
            field=models.CharField(max_length=80, null=True, verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='userbase',
            name='guard_id',
            field=models.CharField(max_length=60, null=True, verbose_name='保镖ID'),
        ),
    ]
