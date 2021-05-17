FROM python:3.8.5

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP "manage.py"
ENV FLASK_ENV "development"
COPY . /usr/src/app

CMD ["flask", "run"]