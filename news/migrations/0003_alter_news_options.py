# Generated by Django 4.1 on 2022-08-19 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options_news_author_alter_news_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-data',), 'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
    ]