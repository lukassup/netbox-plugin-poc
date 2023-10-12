from netbox.extras.plugins import PluginMenu, PluginMenuItem

menu = PluginMenu(
    label='Provisioning',
    icon_class="mdi mdi-hammer",
    groups=[
        ('PROVISIONING', 
            (
                PluginMenuItem(link="plugins:netbox_provisioning:list", link_text="Devices"),
            )
        ),
    ]
)
