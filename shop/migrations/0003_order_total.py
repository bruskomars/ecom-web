# Generated by Django 5.0.1 on 2024-02-02 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
