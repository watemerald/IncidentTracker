FROM python:3.7

copy . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system 

EXPOSE 5000

RUN flask db init
RUN flask db upgrade

CMD ["python", "run.py"]