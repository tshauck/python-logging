FROM kiyoto/fluentd:0.10.56-2.1.1

MAINTAINER kiyoto@treausure-data.com

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install curl

RUN ["/usr/local/bin/gem", "install", "fluent-plugin-record-reformer", "--no-rdoc", "--no-ri"]
RUN ["/usr/local/bin/gem", "install", "fluent-plugin-elasticsearch", "--no-rdoc", "--no-ri"]

RUN mkdir /etc/fluent
ADD fluent.conf /etc/fluent/

ENTRYPOINT ["/usr/local/bin/fluentd", "-c", "/etc/fluent/fluent.conf"]

