# Generated by Django 4.2.3 on 2023-08-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'PcText',
                'verbose_name_plural': 'PcTexts',
            },
        ),
    ]
