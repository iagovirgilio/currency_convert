FROM python:3.12.2-alpine3.19
LABEL mantainer="iagovirgilio@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED  1

COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app

EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /app/requirements.txt && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

CMD ["commands.sh"]
