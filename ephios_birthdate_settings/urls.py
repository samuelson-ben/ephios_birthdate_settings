from django.urls import path
from .views import BirthdateSettingsView

app_name = "ephios_birthdate_settings"

urlpatterns = [
    path(
        "settings/birthdate/",
        BirthdateSettingsView.as_view(),
        name="birthdate_form",
    ),
]
