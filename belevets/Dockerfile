FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt &&\
    mkdir -p /vol/media &&\
    chmod -R 755 /vol
COPY . /code/

