# Generated by Django 3.2.9 on 2022-02-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookstatus',
            fields=[
                ('bsid', models.AutoField(primary_key=True, serialize=False)),
                ('prod_id', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('sell_id', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
                ('d_status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bookstatus',
            },
        ),
    ]