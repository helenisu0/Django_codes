# Generated by Django 4.0.4 on 2022-04-13 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.TextField(default='https://d2slcw3kip6qmk.cloudfront.net/marketing/blog/2019Q1/why-pm-is-important/why-is-project-management-important-header@2x.png'),
        ),
    ]
