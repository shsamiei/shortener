# Generated by Django 4.1.3 on 2022-11-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkshortener', '0005_alter_shortener_shortener'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='shortener',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]