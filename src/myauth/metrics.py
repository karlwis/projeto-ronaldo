from prometheus_client import Counter, Gauge, Histogram

HTTP_REQUESTS_TOTAL = Counter(
    'http_requests_total',
    'Total de requisicoes HTTP',
    ['method', 'endpoint', 'status'],
)

HTTP_REQUEST_DURATION_SECONDS = Histogram(
    'http_request_duration_seconds',
    'Duracao das requisicoes HTTP em segundos',
    ['method', 'endpoint'],
)

HTTP_REQUESTS_IN_PROGRESS = Gauge(
    'http_requests_in_progress',
    'Requisicoes HTTP em andamento',
    ['method'],
)
