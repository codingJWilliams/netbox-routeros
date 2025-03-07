# Generated by Django 3.1.3 on 2021-03-07 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tenancy", "0011_standardize_name_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConfigurationTemplate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("content", models.TextField()),
                (
                    "tenant",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="routeros_configuration_templates",
                        to="tenancy.tenant",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
