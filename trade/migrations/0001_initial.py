# Generated by Django 5.0.6 on 2024-06-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('card_name', models.CharField(help_text='会员卡名称', max_length=100, unique=True, verbose_name='会员卡名称')),
                ('card_price', models.DecimalField(decimal_places=2, help_text='会员卡价格', max_digits=10, verbose_name='会员卡价格')),
                ('duration', models.IntegerField(help_text='有效期', verbose_name='有效期')),
                ('info', models.TextField(help_text='会员卡说明', verbose_name='会员卡说明')),
            ],
            options={
                'verbose_name': '会员卡',
                'verbose_name_plural': '会员卡',
            },
        ),
    ]
