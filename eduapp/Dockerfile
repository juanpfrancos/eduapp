FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["gunicorn", "eduapp.wsgi:application", "--bind", "0.0.0.0:8000"]
