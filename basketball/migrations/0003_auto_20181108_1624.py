# Generated by Django 2.1.2 on 2018-11-08 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketball', '0002_auto_20181108_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': '活动名', 'verbose_name_plural': '活动名'},
        ),
        migrations.AlterModelOptions(
            name='candidate',
            options={'verbose_name': '参赛选手', 'verbose_name_plural': '参赛选手'},
        ),
        migrations.AlterModelOptions(
            name='voterecord',
            options={'verbose_name': '投票记录', 'verbose_name_plural': '投票记录'},
        ),
    ]