# Generated by Django 2.1.7 on 2021-03-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salt', '0002_auto_20210321_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspector',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='saltcheck',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='saltclient',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='saltintype',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='saltlocation',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='saltna',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='saltnew',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='saltrb',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='saltstatus',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='stovenumber',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='team',
            name='remark',
            field=models.CharField(blank=True, help_text='备注', max_length=256, null=True, verbose_name='备注'),
        ),
    ]
