FROM python:3.7

copy . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system 

EXPOSE 5000

RUN flask db upgrade
RUN flask db upgrade

CMD ["python", "app.py"]