# Generated by Django 4.2.7 on 2023-11-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_category_options_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('published', 'published'), ('draft', 'draft')], default='draft', max_length=100),
        ),
    ]
