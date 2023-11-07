FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/training/scripts:${PATH}"

WORKDIR /training

COPY requirements.txt /training/

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        binutils \
        gcc \
        libpq-dev \
        python3-dev \
    ; \
    useradd -c "App User" \
        --home-dir /training \
        --shell /bin/sh \
        --create-home \
        --uid 1000 \
        app \
    ; \
    pip install --no-cache-dir --upgrade pip; \
    pip install --no-cache-dir --upgrade setuptools; \
    pip install --no-cache-dir -r requirements.txt; \
    chown -R app:app /training; \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
    rm -rf /var/lib/apt/lists/*

COPY . /training/

USER 1000

CMD ["entrypoint.sh"]
