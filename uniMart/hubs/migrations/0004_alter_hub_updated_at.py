# Generated by Django 5.1.7 on 2025-03-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0003_hub_admin_hub_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
