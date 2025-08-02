from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AboutView(TemplateView):
    template_name = "core/about.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "core/profile.html"
