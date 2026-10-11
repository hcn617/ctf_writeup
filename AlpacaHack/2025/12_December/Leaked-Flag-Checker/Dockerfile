FROM --platform=linux/amd64 ubuntu:24.04

WORKDIR /work

RUN apt-get update && apt-get install -y python3

COPY challenge /work/challenge
COPY solve.py /work/solve.py

RUN chmod +x /work/challenge
