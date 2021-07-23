FROM ubuntu

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y libmysqlclient-dev

WORKDIR /app

COPY ./requirements.txt ./requirements.txt 

RUN pip3 install -r ./requirements.txt

EXPOSE 5002

COPY . . 

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]