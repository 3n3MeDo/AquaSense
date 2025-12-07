from django.shortcuts import redirect
from django.urls import reverse

class AdminRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
            # Define paths exempt from redirection
            # We must allow /admin/ to prevent infinite loops
            # We must allow /logout/ so they can sign out
            if not request.path.startswith('/admin/') and not request.path == '/logout/':
                return redirect('/admin/')

        response = self.get_response(request)
        return response
