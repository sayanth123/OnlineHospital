# Generated by Django 3.2.5 on 2021-07-13 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_patient_pat_msg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='pat_msg',
            new_name='message',
        ),
    ]