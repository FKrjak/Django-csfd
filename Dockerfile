FROM python:3.8.16-slim AS builder
EXPOSE 8000
RUN mkdir /app
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
RUN apt-get update
RUN apt-get -y install make
COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
