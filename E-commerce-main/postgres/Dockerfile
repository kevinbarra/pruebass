FROM postgres:16.2-alpine

ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=12345
ENV POSTGRES_DB=users_db

COPY init.sql /docker-entrypoint-initdb.d/
