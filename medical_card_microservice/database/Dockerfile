FROM postgres:13-alpine

COPY ./scripts/startup.sh /docker-entrypoint-initdb.d/startup.sh
COPY ./scripts /opt/app/scripts