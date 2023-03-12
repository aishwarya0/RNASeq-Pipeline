FROM python:3.8.11-buster
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;
RUN apt-get -y update && \
    apt-get clean;
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

WORKDIR /
COPY seq_trim.py /scripts/
RUN wget "https://github.com/usadellab/Trimmomatic/files/5854850/Trimmomatic-0.38.zip" -O Trimmomatic-0.38.zip && \
    unzip Trimmomatic-0.38.zip 