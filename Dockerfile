###################################
#
# CYBR8470 Dev Docker Container
# @author Matt Hale
#
###################################

# Pull base image.
FROM python:2.7.13
ENV PYTHONUNBUFFERED 1

# Setup linkages to code repositories and add to image

WORKDIR /var/www/backend

ADD requirements.txt /var/www/backend/
RUN pip install -r requirements.txt
ADD . /var/www/backend/

EXPOSE 5000

