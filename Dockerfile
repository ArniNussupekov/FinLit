FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /finLit
WORKDIR /FinLit
COPY . /FinLit
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["/FinLit/django.sh"]
