# Generated by Django 2.0.4 on 2018-06-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_learningtheme_ready'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='initial_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='theme',
            name='referenceContent',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
