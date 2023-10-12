from netbox.extras.plugins import PluginTemplateExtension

from . import config as plugin


class DeviceContent(PluginTemplateExtension):
    model = 'dcim.device'

    def left_page(self):
        return ''

    def right_page(self):
        return ''

    def full_width_page(self):
        return ''

    def buttons(self):
        return self.render('device_detail_buttons.html')

    def list_buttons(self):
        return self.render('device_list_buttons.html')


template_extensions = [DeviceContent]
