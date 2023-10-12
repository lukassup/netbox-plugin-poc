import django_tables2 as tables

from netbox.netbox.tables import NetBoxTable

from netbox.netbox.dcim.models import Device


class DeployableTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    
    class Meta(NetBoxTable.Meta):
        model = Device
        #fields = ('pk','id', 'name', 'status')
        fields = '*'

