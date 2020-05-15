# Generated by Django 3.0.5 on 2020-05-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0006_auto_20200502_0705'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='contestquestion',
            name='name of constraint',
        ),
        migrations.RenameField(
            model_name='contestquestion',
            old_name='cId',
            new_name='contest',
        ),
        migrations.AddField(
            model_name='contestquestion',
            name='qtype',
            field=models.CharField(choices=[('MCQ', 'Multiple Choice Question'), ('Coding', 'Coding Question')], default='MCQ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='contestquestion',
            constraint=models.UniqueConstraint(fields=('contest', 'qno'), name='name of constraint'),
        ),
    ]
