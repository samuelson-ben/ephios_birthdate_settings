from ephios.core.plugins import PluginConfig


class PluginApp(PluginConfig):
    name = "ephios_birthdate_settings"

    class EphiosPluginMeta:
        name = "ephios_birthdate_settings"
        author = "Ben Samuelson <ben.samuelson@fiteka.de>"
        description = "Allows user to set his own birthday once"

    def ready(self):
        from . import signals  # NOQA
