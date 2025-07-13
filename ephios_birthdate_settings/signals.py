from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.template.loader import render_to_string
from ephios.core.signals import homepage_info

@homepage_info.connect
def show_birthdate_card(sender, request, **kwargs):
    user = request.user
    if user and not getattr(user, "date_of_birth", None):
        return render_to_string("ephios_birthdate_settings/dashboard_card.html", request=request)
    return "<p>Geburtsdatum erfolgreich gesetzt.</p>"
