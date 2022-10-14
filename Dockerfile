FROM python:3.9-slim

ENV PATH="/training/scripts:${PATH}"

WORKDIR /training

COPY requirements.txt /training/

RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        curl \
        gcc \
        g++ \
        libicu-dev \
        pkg-config \
        python3-dev \
        python3-icu \
    ; \
    useradd -c "App User" \
        --home-dir /app \
        --shell /bin/sh \
        --create-home \
        --uid 1000 \
        app \
    ; \
    pip install --upgrade pip; \
    pip install --upgrade setuptools; \
    pip install -r requirements.txt; \
    chown -R app:app /training

COPY . /training/

USER 1000

CMD ["entrypoint.sh"]
