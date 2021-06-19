# image from nginx to allow to run nginx in 'unprivileged' mode (no root user)
FROM nginxinc/nginx-unprivileged:1-alpine

LABEL maintainer="rbn_mrz"

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

# temporarly switches to root user for commands
USER root

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

# switch back to unvprivileged user
USER nginx