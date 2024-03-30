FROM tiangolo/uwsgi-nginx-flask:python3.10

ENV LISTEN_PORT 5055

EXPOSE 5055

COPY . /app

RUN sed -i "s/= main/= app/" /app/uwsgi.ini
