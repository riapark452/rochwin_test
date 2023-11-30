FROM python:3.9.17-bookworm
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
ADD . /code/
RUN pip install -r requirements.txt
