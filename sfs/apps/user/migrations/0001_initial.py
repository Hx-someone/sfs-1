# Generated by Django 2.1.7 on 2021-03-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=1, verbose_name='版本号')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, help_text='更新时间', verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除')),
                ('remark', models.CharField(default=' ', help_text='备注', max_length=256, verbose_name='备注')),
                ('user_name', models.CharField(max_length=18, verbose_name='用户名')),
                ('password', models.CharField(max_length=18, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'tb_users',
                'ordering': ['update_time', 'id'],
            },
        ),
    ]