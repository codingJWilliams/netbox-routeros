from netbox_routeros.models import ConfigurationTemplate, ConfiguredDevice
from tenancy.filtersets import TenancyFilterSet
from netbox.filtersets import BaseFilterSet, NetBoxModelFilterSet


class ConfiguredDeviceFilterSet(
    BaseFilterSet, TenancyFilterSet
):
    class Meta:
        # TODO: Include device fields
        model = ConfiguredDevice
        fields = [
            "device",
            "configuration_template",
            "last_config_fetched_at",
            "last_config_pushed_at",
        ]


class ConfigurationTemplateFilterSet(
    BaseFilterSet, TenancyFilterSet
):
    class Meta:
        model = ConfigurationTemplate
        fields = ["id", "name", "slug"]
