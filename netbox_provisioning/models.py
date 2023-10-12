import uuid
from django.utils.translation import gettext as _
from django.db import models
from netbox.netbox.models import NetBoxModel
from dcim.models.devices import Device


class ProvisioningResult(NetBoxModel):

    class Status(models.IntegerChoices):
        UNKNOWN = 3, _('Unknown')
        RUNNING = 2, _('Running')
        FAILED = 1, _('Failed')
        SUCCESS = 0, _('Success')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device = models.ForeignKey(Device, on_delete=models.CASCADE )
    status = models.CharField(choices=Status.choices)
    result = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('updated_at',)
