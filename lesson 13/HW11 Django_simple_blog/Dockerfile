FROM alpine:3.16

RUN apk update
RUN apk add python3-dev py3-pip postgresql-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers

WORKDIR /opt/wallpaper

RUN pip install pipenv

COPY . ./

RUN pipenv sync

ENTRYPOINT ["pipenv", "run", "python3", "manage.py"]

CMD ["runserver"]



