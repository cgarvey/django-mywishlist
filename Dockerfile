FROM python:2
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install mysqlclient
RUN pip install -r requirements.txt
