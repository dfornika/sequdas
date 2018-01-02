import os 

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

from graphene_django.views import GraphQLView
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view

class DRFAuthenticatedGraphQLView(GraphQLView):
    # custom view for using DRF TokenAuthentication with graphene GraphQL.as_view()
    # all requests to Graphql endpoint will require token for auth, obtained from DRF endpoint
    # https://github.com/graphql-python/graphene/issues/249
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(DRFAuthenticatedGraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticated,))(view)
        view = authentication_classes((JSONWebTokenAuthentication,))(view)
        view = api_view(['POST'])(view)
        return view

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
