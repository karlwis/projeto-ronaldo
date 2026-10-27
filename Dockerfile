FROM python:3.14-slim

WORKDIR /app

COPY requirements-lock.txt .

RUN pip install --no-cache-dir --only-binary=:all: --require-hashes -r requirements-lock.txt

COPY src/ /app/src/

RUN useradd --create-home --shell /usr/sbin/nologin appuser \
    && chown -R appuser:appuser /app

USER appuser

WORKDIR /app/src

EXPOSE 8000

CMD ["gunicorn", "meu_projeto.wsgi:application", "--bind", "0.0.0.0:8000"]
