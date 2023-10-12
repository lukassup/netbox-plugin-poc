from collections import defaultdict

from django.contrib.auth.mixins import PermissionRequiredMixin
from netbox.netbox.views import generic
# from netbox.netbox.views.generic.base import BaseMultiObjectView
# from netbox.netbox.views.generic.mixins import TableMixin

from dcim.models import Device

from . import tables

class ProvisioningListView(generic.ObjectListView):
    queryset = Device.objects.filter(status='staged')
    table = tables.ProvisioningListTable
    actions = ('provision', 'bulk_provision')
    action_perms = defaultdict(set, **{
        'provision': {'change'},
        'bulk_provision': {'change'},
    })


class ProvisioningView(generic.ObjectView):
    queryset = Device.objects.filter(status='staged')


class ProvisioningProvisionView(generic.ObjectView):
    queryset = Device.objects.filter(status='staged')

class ProvisioningBulkProvisionView(generic.ObjectView):
    queryset = Device.objects.filter(status='staged')
