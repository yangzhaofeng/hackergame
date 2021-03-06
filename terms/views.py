from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic

from .models import Terms


class TermsList(LoginRequiredMixin, generic.ListView):
    template_name = 'terms/terms_list.html'

    def get_queryset(self):
        return Terms.current_terms()

    @staticmethod
    def post(request):
        request.user.terms_set.set(request.POST.getlist('terms'))
        return redirect(settings.TERMS_REDIRECT_URL)
