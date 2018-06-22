# Generated by Django 2.0.4 on 2018-06-22 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_problem_referenceinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difficult',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='student.Problem'),
        ),
        migrations.AlterField(
            model_name='difficult',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='themes', to='student.Theme'),
        ),
    ]