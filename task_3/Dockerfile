FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install requests

COPY script.py ./script.py

CMD ["python3", "script.py"]
