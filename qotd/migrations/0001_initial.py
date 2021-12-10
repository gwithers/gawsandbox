# Generated by Django 4.0 on 2021-12-09 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the quote', max_length=256)),
                ('quote_type', models.CharField(help_text='Type of concrete quote', max_length=10)),
            ],
            options={
                'verbose_name': 'Base Quote',
                'verbose_name_plural': 'Base Quotes',
            },
        ),
        migrations.CreateModel(
            name='MOTD',
            fields=[
            ],
            options={
                'verbose_name': 'Message of the Day',
                'verbose_name_plural': 'Daily Messages',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('qotd.basequote',),
        ),
        migrations.CreateModel(
            name='MOTW',
            fields=[
            ],
            options={
                'verbose_name': 'Message of the Week',
                'verbose_name_plural': 'Weekly Messages',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('qotd.basequote',),
        ),
    ]