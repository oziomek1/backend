FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    rm -rf /var/lib/apt/lists/*

COPY . .

WORKDIR .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["run.py"]
