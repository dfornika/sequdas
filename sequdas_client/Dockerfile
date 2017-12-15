FROM continuumio/miniconda3

RUN mkdir -p /opt/sequdas_client
RUN mkdir -p /data/miseq

COPY requirements.txt sequdas_client.py sequdas_client db config /opt/sequdas_client/
RUN conda create -y -n sequdas_client python=3
ENV PATH /opt/conda/envs/sequdas_client/bin:$PATH
RUN /bin/bash -c "source activate sequdas_client" \
    && pip install -r /opt/sequdas_client/requirements.txt

CMD python /opt/sequdas_client/sequdas_client.py -c /opt/sequdas_client/config/config.ini.docker
