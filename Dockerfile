FROM tiangolo/uwsgi-nginx-flask:python3.10

# WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN mv /app/prestart.sh /app/prestart.sh.backup
RUN sed -i "s/= main/= app/" /app/uwsgi.ini

ENV LISTEN_PORT 5055

EXPOSE 5055