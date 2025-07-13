from django.urls import path
from .views import BirthdateSettingsView

urlpatterns = [
    path(
        "settings/birthdate/",
        BirthdateSettingsView.as_view(),
        name="ephios_birthdate_settings",
    ),
]
