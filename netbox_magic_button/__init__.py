from netbox.extras.plugins import PluginConfig

class NetboxMagicButtonConfig(PluginConfig):
    name = 'netbox_magic_button'
    verbose_name = 'NetBox Magic Button'
    description = 'The Button'
    version = '0.1.0'
    base_url = 'the-button'

config = NetboxMagicButtonConfig
