from django.utils.deprecation import MiddlewareMixin


# FIXME:
class DisableCSRF(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)