FROM ubuntu

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

WORKDIR /app

COPY ./requirements.txt ./requirements.txt 

RUN pip3 install -r ./requirements.txt

EXPOSE 5001

COPY . . 

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]