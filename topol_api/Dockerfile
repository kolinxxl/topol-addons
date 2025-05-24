FROM ghcr.io/home-assistant/amd64-base-python:3.11

ENV LANG C.UTF-8

COPY ./app /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "/app/run.sh" ]
