# Generated by Django 4.1.4 on 2022-12-16 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_article_user_id_alter_timeforofficial_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='default', max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_id',
            field=models.CharField(default='default', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_url',
            field=models.URLField(default='default'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user_id',
            field=models.OneToOneField(default='default', on_delete=django.db.models.deletion.CASCADE, to='app1.user'),
        ),
        migrations.AlterField(
            model_name='timeforofficial',
            name='user_id',
            field=models.OneToOneField(default='default', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app1.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default='default', max_length=200, primary_key=True, serialize=False),
        ),
    ]
