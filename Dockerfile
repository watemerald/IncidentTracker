FROM python:3.7

RUN pip install pipenv gunicorn

COPY . /app
WORKDIR /app

RUN pipenv install --system

CMD ["python", "run.py"]