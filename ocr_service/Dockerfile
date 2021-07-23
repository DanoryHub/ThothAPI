FROM ubuntu

RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y libmysqlclient-dev

WORKDIR /app

RUN mkdir images/

COPY ./requirements.txt ./requirements.txt 

COPY ./rus.traineddata /usr/share/tesseract-ocr/4.00/tessdata/rus.traineddata

RUN pip3 install -r ./requirements.txt

EXPOSE 5000

COPY . . 

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]