# Pull base image
FROM python:3.6-alpine

# System env variables
ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /src
WORKDIR /src

# Copy project
COPY . /src

# Install project dependencies
RUN apk update && \ 
    apk add postgresql-dev gcc musl-dev && \
    pip install -r requirements.txt