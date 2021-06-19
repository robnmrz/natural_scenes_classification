FROM python:3.8-alpine

# adding image label for maintainer
LABEL maintainer="rbn_mrz"

# Updating alpine and installing tmp. packages to 
# use pip with (will be removed later)
RUN apk update
RUN apk add --update --no-cache --virtual .tmp \ 
    gcc libc-dev musl-dev linux-headers

COPY ./requirements.txt /requirements.txt

# Install python dependencies from requirements.txt
RUN pip install -r /requirements.txt

# Setting up working directory
RUN mkdir app
COPY ./app /app
WORKDIR /app

# Creates new user for docker user (less rights than root user)
RUN adduser -D user

# Switch to less priviledged user
USER user

# Script to enter application
CMD ["uwsgi", "app.ini"]