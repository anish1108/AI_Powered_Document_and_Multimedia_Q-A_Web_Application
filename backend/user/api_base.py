from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class ApiBaseView(View):
    """
    Base class for all API views.
    CSRF disabled safely for APIs.
    """
    pass
