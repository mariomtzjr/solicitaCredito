FROM python:3.6-alpine

ENV PYTHONUNBUFFERED=1

# Add create super user
# ADD ./web/bin/install.sh install.sh
# RUN chmod +x install.sh

#Install extra libs for mysql
RUN apk add --update --upgrade --no-cache --virtual .build-deps\
    musl-dev \
    gcc \
    postgresql-dev \
    py-imaging \
    jpeg-dev \
    zlib-dev \
    py3-reportlab \
    glib \
    git \
    ca-certificates \
    nano \
    curl

# Add requirements.txt file to container
ADD ./web/requirements.txt /requirements.txt
ADD ./web/dev.dockerfile /dev.dockerfile

# Update pip & install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

# Creation of the workdir
RUN mkdir /code

WORKDIR /code

ADD ./ /code/
