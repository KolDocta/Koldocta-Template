# import base image
FROM ubuntu:trusty

# install system-wide dependencies,
# python and the build-time dependencies for c modules
RUN apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
python python-dev python-pip python-lxml build-essential

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# server ports
EXPOSE 5000

# set env vars for the server
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT "False"
ENV CELERYBEAT_SCHEDULE_FILENAME /tmp/celerybeatschedule.db

# install server dependencies
COPY requirements.txt /tmp/requirements.txt
RUN cd /tmp && pip install -U -r /tmp/requirements.txt
