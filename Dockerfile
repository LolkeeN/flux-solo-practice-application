FROM alpine:3.14

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip

RUN ["sh", "-c", "echo Flask==3.1.2 > requirements.txt"]
RUN ["sh", "-c", "pip3 install -r requirements.txt"]

COPY app.py /app/app.py
COPY VERSION /app/VERSION
WORKDIR /app

CMD ["python3", "app.py"]