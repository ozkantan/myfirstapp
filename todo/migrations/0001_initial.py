# Generated by Django 2.2.7 on 2019-12-20 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoAppTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('completed', models.BooleanField(verbose_name='Durum')),
                ('email', models.EmailField(default='', max_length=255)),
                ('send_date', models.DateTimeField(null=True, verbose_name='Hatırlatma Tarihi')),
                ('taskdurum', models.BooleanField(verbose_name='Task Durum')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Todo List',
            },
        ),
    ]
