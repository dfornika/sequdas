FROM python:3.6

RUN apt-get update && apt-get install -y vim

RUN mkdir -p /app/sequdas_server
COPY sequdas_server.py sequdas_server requirements.txt /app/sequdas_server/
RUN pip install -r /app/sequdas_server/requirements.txt
RUN pip install -f https://github.com/Illumina/interop/releases/latest interop

CMD python /app/sequdas_server/sequdas_server.py
