import os 

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView

class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass

class ReactAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as file:
                return HttpResponse(file.read())
        except :
            return HttpResponse(
                """
                index.html not found ! build your React app !!
                """,
                status=501,
            )
