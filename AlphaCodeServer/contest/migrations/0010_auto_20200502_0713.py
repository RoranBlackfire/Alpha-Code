# Generated by Django 3.0.5 on 2020-05-02 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0009_auto_20200502_0711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='q_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='testcase',
            old_name='q_id',
            new_name='question',
        ),
    ]
