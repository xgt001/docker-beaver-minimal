FROM gliderlabs/alpine:3.3

RUN apk add --update \
    python \
    py-pip \
  && pip install beaver \
  && rm -rf /var/cache/apk/*

RUN mkdir /app
WORKDIR /app

COPY beaver.conf /app/

CMD ["/usr/bin/beaver", "-c","/app/beaver.conf","-t","sqs"]
