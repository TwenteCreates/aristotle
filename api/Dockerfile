FROM alpine:3.10

ENV PYTHONUNBUFFERED=0
ARG TZ=Europe/Amsterdam

WORKDIR /usr/src/app

RUN apk add --update --no-cache python3 mailcap && \
    find / -type d -name __pycache__ -exec rm -r {} +   && \
    rm -r /usr/lib/python*/ensurepip                    && \
    rm -r /usr/lib/python*/lib2to3                      && \
    rm -r /usr/lib/python*/turtledemo                   && \
    rm /usr/lib/python*/turtle.py                       && \
    rm /usr/lib/python*/webbrowser.py                   && \
    rm /usr/lib/python*/doctest.py                      && \
    rm /usr/lib/python*/pydoc.py                        && \
    rm -rf /root/.cache /var/cache /usr/share/terminfo

COPY requirements.txt .

RUN mkdir -p /var/cache/apk \
    && apk add --update --no-cache --virtual .build-deps \
		gcc \
		g++ \
		musl-dev \
        python3-dev \
        linux-headers \
        tzdata \
	&& cp /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && pip3 --no-cache-dir install -r requirements.txt \
    && apk --no-cache del .build-deps \
    && rm -r /var/cache

COPY . .

RUN python3 manage.py collectstatic
# && \
#    python3 manage.py makemigrations --no-input && \
#    python3 manage.py migrate --no-input

EXPOSE 8000

ENTRYPOINT ["uwsgi", "--ini", "uwsgi.ini"]
