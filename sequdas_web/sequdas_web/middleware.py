from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', '')
        print('***' + token + '***')
        if not token.startswith('JWT'):
            return
        jwt_auth = JSONWebTokenAuthentication()
        auth = None
        try:
            auth = jwt_auth.authenticate(request)
        except Exception:
            return
        request.user = auth[0]
