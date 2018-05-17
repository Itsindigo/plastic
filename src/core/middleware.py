from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class AppendSlashMiddleware:
    """
    Appends slash to any incoming requests, this way we can resolve server side urls with certainty before falling
    back to our Single-Page-App (SPA) routing configuration.

    Duplicates some logic with the CommonMiddleware, however CommonMiddleware expects 404's to be handled in the Django
    URL routing config, rather than in the client.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.path.endswith('/'):
            return self.get_response(request)
        else:
            return HttpResponsePermanentRedirect(self.get_full_path_with_slash(request))

    def get_full_path_with_slash(self, request):
        """
        Return the full path of the request with a trailing slash appended.

        Raise a RuntimeError if settings.DEBUG is True and request.method is
        POST, PUT, or PATCH.
        """
        new_path = request.get_full_path(force_append_slash=True)
        if settings.DEBUG and request.method in ('POST', 'PUT', 'PATCH'):
            raise RuntimeError(
                "You called this URL via %(method)s, but the URL doesn't end "
                "in a slash and you have APPEND_SLASH set. Django can't "
                "redirect to the slash URL while maintaining %(method)s data. "
                "Change your form to point to %(url)s (note the trailing "
                "slash), or set APPEND_SLASH=False in your Django settings." % {
                    'method': request.method,
                    'url': request.get_host() + new_path,
                }
            )
        return new_path