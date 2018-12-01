FROM alpine:3.8

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

RUN pip3 --no-cache-dir install -r requirements.txt \
    && echo $TZ > /etc/timezone

COPY . .

CMD ["python3", "manage.py", "runserver"]
