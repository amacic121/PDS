FROM python

WORKDIR /Client

COPY . /Client

RUN pip install requests

EXPOSE 8080

CMD ["python" , "client.py"]