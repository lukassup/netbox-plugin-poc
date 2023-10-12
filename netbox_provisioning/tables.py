import django_tables2 as tables
# from netbox.netbox.tables import NetBoxTable
from netbox.dcim.tables import DeviceTable
from netbox.netbox.tables.columns import ActionsItem, ActionsColumn
from dcim.models import Device

# class ProvisioningActionsColumn(ActionsColumn):
#     actions = {
#         'provision': ActionsItem('Provision', 'hammer', 'change', 'warning'),
#     }

#     def __init__(self, *args, **kwargs):
#         tables.Column.__init__(self, *args, **kwargs)
#         self.extra_buttons = ''
#         self.split_actions = False

class ProvisioningListTable(DeviceTable):
    # actions = ProvisioningActionsColumn()

    class Meta(DeviceTable.Meta):
        model = Device
        # fields = ('*',)
