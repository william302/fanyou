# Generated by Django 2.1.2 on 2018-10-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='ID_number',
            field=models.IntegerField(verbose_name='身份证号码'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='commission_rate',
            field=models.DecimalField(decimal_places=2, max_digits=3, verbose_name='佣金比例'),
        ),
        migrations.AlterField(
            model_name='merchant',
            name='phone_number',
            field=models.IntegerField(max_length=20, verbose_name='联系电话'),
        ),
    ]
