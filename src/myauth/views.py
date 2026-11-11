from django.http import HttpResponse
from django.views.decorators.http import require_GET


@require_GET
def home(request):
    return HttpResponse("Projeto Ronaldo")


@require_GET
def health(request):
    return HttpResponse("OK")


from django.http import HttpResponse
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest


@require_GET
def metrics(request):
    return HttpResponse(
        generate_latest(),
        content_type=CONTENT_TYPE_LATEST,
    )
