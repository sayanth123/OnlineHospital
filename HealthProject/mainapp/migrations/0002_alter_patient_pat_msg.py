# Generated by Django 3.2.5 on 2021-07-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='pat_msg',
            field=models.TextField(max_length=300),
        ),
    ]
