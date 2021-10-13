FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /app
#RUN apt-get upgrade -y gcc
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 8000