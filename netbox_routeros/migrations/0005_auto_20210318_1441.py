# Generated by Django 3.1.3 on 2021-03-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_routeros", "0004_configureddevice_extra_configuration"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="configureddevice",
            name="last_config_pushed",
        ),
        migrations.AddField(
            model_name="configureddevice",
            name="last_verbose_config_fetched",
            field=models.TextField(blank=True, default=""),
        ),
    ]
