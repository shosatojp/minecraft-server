FROM alpine:3.12

RUN apk update && \
    apk add nginx zip

COPY default.conf /etc/nginx/conf.d/
RUN mkdir -p /run/nginx /pub
RUN rm -f /var/log/nginx/access.log && \
    ln -s /dev/stdout /var/log/nginx/access.log

CMD zip -r /pub/mods.zip /pub/mods && \
    zip -r /pub/config.zip /pub/config && \
    nginx -g "daemon off;"
EXPOSE 8080
