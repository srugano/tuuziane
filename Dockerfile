# Use a Python runtime as base image
FROM python:3.12-slim-bookworm

# Add user that will be used in the container.
RUN useradd wagtail

# Port used by this container to serve HTTP.
EXPOSE 8000

# Set environment variables.
# 1. Force Python stdout and stderr streams to be unbuffered.
# 2. Set PORT variable that is used by Gunicorn. This should match "EXPOSE"
#    command.
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages and Node.js
RUN apt-get update --yes --quiet && \
    apt-get install --yes --quiet --no-install-recommends \
        build-essential \
        libpq-dev \
        libjpeg62-turbo-dev \
        zlib1g-dev \
        libwebp-dev \
        curl \
        gnupg \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g webpack \
    && npm install -g webpack-cli \
    && rm -rf /var/lib/apt/lists/*

# Install the application server.
RUN pip install "gunicorn==20.0.4"

# Install the project requirements.
# COPY requirements.txt /
# RUN pip install -r /requirements.txt

# Use /app folder as a directory where the source code is stored.
WORKDIR /app

# Set this directory to be owned by the "wagtail" user. This Wagtail project
# uses SQLite, the folder needs to be owned by the user that
# will be writing to the database file.
RUN chown wagtail:wagtail /app

# Copy the source code of the project into the container.
COPY --chown=wagtail:wagtail . .

# Set npm config to use app-relative paths as root first
RUN npm config set cache /app/.npm/_cacache --global && \
    npm config set update-notifier false --global

# Create npm cache directories and set permissions
RUN mkdir -p /app/.npm/_logs /app/.npm/_cacache && \
    chown -R wagtail:wagtail /app/.npm

# Switch to wagtail user
USER wagtail

# Build frontend
WORKDIR /app/vue-tuuziane
RUN npm install && npm install -D webpack-cli vue-loader style-loader css-loader
RUN npm run build
WORKDIR /app

# Collect static files.
RUN python manage.py collectstatic --noinput --clear

# Runtime command that executes when "docker run" is called, it does the
# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
CMD set -xe; python manage.py migrate --noinput; gunicorn tuuziane.wsgi:application
