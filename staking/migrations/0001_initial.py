# Generated by Django 2.2.11 on 2021-11-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StakingCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True, verbose_name='Название')),
                ('logo', models.CharField(blank=True, max_length=120, null=True, verbose_name='Логотип')),
                ('dayplan', models.CharField(blank=True, max_length=120, null=True, verbose_name='Дни')),
                ('procent', models.CharField(blank=True, max_length=120, null=True, verbose_name='Процент')),
                ('slug', models.SlugField(blank=True, default=None, null=True, verbose_name='Транслит(Не трогать)')),
                ('is_active', models.BooleanField(default=True, verbose_name='В наличии')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
            ],
            options={
                'verbose_name': 'Монета Стекинга',
                'verbose_name_plural': 'Монета Стекинга',
            },
        ),
    ]