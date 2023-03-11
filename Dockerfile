FROM python:3.8.11-buster
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;
RUN apt-get -y update && \
    apt-get clean;
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME
#RUN apt-get -y update && apt-get clean
#RUN apt install default-jre
WORKDIR /
COPY fastqc_parser.py /scripts/
RUN apt-get -y install fastqc && apt-get clean;