FROM python:3-alpine
LABEL Maintainer="ilnar20"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY web-app.py ./

ENV AUTHOR=Ilnar
ENV UUID="b77d110c-79af-4095-9e48-2d1d4f6e680a"
ENV PYTHONUNBUFFERED=1

RUN addgroup -S webapp && adduser -S webapp -G webapp

USER webapp

CMD [ "python", "./web-app.py"]

EXPOSE 8000