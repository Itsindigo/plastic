from django.views.generic import View
from django.http import JsonResponse


class JsonView(View):

    http_method_names = ['head', 'options', 'trace']
    permitted_content_types = ['application/json']

    def dispatch(self, request, *args, **kwargs):
        if self.request.content_type not in self.permitted_content_types:
            return self._bad_content_type()

        return super(JsonView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            response = self.post_data(request, *args, **kwargs)
        except Exception as e:
            error = getattr(e, 'message', 'Unknown Error.')
            return JsonResponse({'errors': error}, status=500)

        return response

    def get(self, request, *args, **kwargs):
        try:
            response = self.get_data(request, *args, **kwargs)
        except Exception as e:
            error = getattr(e, 'message', 'Unknown Error.')
            return JsonResponse({'errors': error}, status=500)

        return response

    def get_data(self, request, *args, **kwargs):
        raise NotImplementedError('get_data not implemented by superclass')

    def post_data(self, request, *args, **kwargs):
        raise NotImplementedError('post_data not implemented by superclass')

    def _bad_content_type(self):
        return JsonResponse({'errors': 'Content-Type specified not supported'}, status=415)

