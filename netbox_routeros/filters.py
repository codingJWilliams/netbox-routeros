from netbox_routeros.models import ConfigurationTemplate, ConfiguredDevice
from tenancy.filtersets import TenancyFilterSet
from netbox.filtersets import (
    BaseFilterSet
    
)


class ConfiguredDeviceFilterSet(
    BaseFilterSet
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
    BaseFilterSet
):
    class Meta:
        model = ConfigurationTemplate
        fields = ["id", "name", "slug"]
