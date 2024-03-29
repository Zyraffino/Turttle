# Generated by Django 2.2.7 on 2019-11-27 15:05

import article.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categroy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
                ('description', models.CharField(blank=True, max_length=144)),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144)),
                ('description', models.CharField(blank=True, max_length=144)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('thumbnail', models.ImageField(default='media/article/article_default.jpeg', upload_to=article.utils.PathAndRename('/article'))),
                ('url', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Categroy')),
            ],
        ),
    ]
