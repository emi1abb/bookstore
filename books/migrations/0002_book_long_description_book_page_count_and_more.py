# Generated by Django 5.0.3 on 2024-03-21 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='long_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='page_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='short_description',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnail_url',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
