FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y nginx python3 && \
    rm -rf /var/lib/apt/lists/*

COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/entrypoint.sh /entrypoint.sh
COPY generate-nes-html.py /generate-nes-html.py

WORKDIR /var/www/html

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]
