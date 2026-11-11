from time import perf_counter

from .metrics import (
    HTTP_REQUESTS_TOTAL,
    HTTP_REQUEST_DURATION_SECONDS,
    HTTP_REQUESTS_IN_PROGRESS,
)


class PrometheusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        method = request.method
        start_time = perf_counter()

        HTTP_REQUESTS_IN_PROGRESS.labels(method=method).inc()

        try:
            response = self.get_response(request)
            status = str(response.status_code)

            if request.path != '/metrics/':
                match = getattr(request, 'resolver_match', None)
                endpoint = (match.route or '/') if match else 'unmatched'

                HTTP_REQUESTS_TOTAL.labels(
                    method=method,
                    endpoint=endpoint,
                    status=status,
                ).inc()

                HTTP_REQUEST_DURATION_SECONDS.labels(
                    method=method,
                    endpoint=endpoint,
                ).observe(perf_counter() - start_time)

            return response

        finally:
            HTTP_REQUESTS_IN_PROGRESS.labels(method=method).dec()
