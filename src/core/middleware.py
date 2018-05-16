from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class AppendSlashMiddleware:
    """
    Functionally very similar to CommonMiddleware. However appends a slash before request is executed.
    However, this app runs a Single-Page-App, unlike a typical Django setup which tries to resolve your URL, if a 404
    is returned, Django will append a slash and try again, and possibly resolve the URL, before 404'ing.

    In this instance we are handling 404's in the Single-Page-App, and a match all URL is the default fallback,
    there is then a separate routing module in JavaScript land which may throw a 404 page further up the line.

    Long and short, we need to append a slash before the request is processed in order to guarantee lookup on our
    server routes.
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