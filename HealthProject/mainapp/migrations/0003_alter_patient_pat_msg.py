# Generated by Django 3.2.5 on 2021-07-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_patient_pat_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='pat_msg',
            field=models.CharField(max_length=300),
        ),
    ]