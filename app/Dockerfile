FROM python:3.9-slim
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app