# Generated by Django 3.2.9 on 2022-01-31 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='Userreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'userreg',
            },
        ),
    ]
