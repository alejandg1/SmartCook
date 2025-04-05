FROM postgres:16

COPY .env /etc/environment

EXPOSE 5432
