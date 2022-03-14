FROM python:3.9.10

# RUN conda install --quiet --yes \
#    'mlflow=1.0.0' \
#    'psycopg2'

WORKDIR /home

COPY requirements.txt .

RUN pip install -r requirements.txt

