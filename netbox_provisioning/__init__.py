from netbox.extras.plugins import PluginConfig

class NetboxProvisioningConfig(PluginConfig):
    name = 'netbox_provisioning'
    verbose_name = 'Netbox Provisioning'
    description = 'Netbox Provisioning'
    version = '0.1.0'
    base_url = 'provisoning'

config = NetboxProvisioningConfig
