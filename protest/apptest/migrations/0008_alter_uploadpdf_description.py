# Generated by Django 4.2.1 on 2023-11-05 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadpdf',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
