FROM ubuntu:14.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python-dev python-pip

RUN pip install fluent-logger colorlog
RUN pip install PyYaml
ADD ./logging-test.py /logging-test.py
ADD ./*.yaml /

CMD ["python", "/logging-test.py"]
