FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /tutorials

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "migrate"]
