# Generated by Django 3.2.9 on 2022-02-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreg',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
