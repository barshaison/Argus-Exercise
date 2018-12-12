FROM ubuntu:16.04

MAINTAINER Daniel
RUN apt-get update -y && \
   apt-get install -y python-pip python3-dev
RUN pip install requests
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
