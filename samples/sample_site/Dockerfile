FROM ubuntu:xenial

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        convmv \
        php7.0-cli \
        php-net-ftp \
    && rm -rf /var/lib/apt/lists/*
