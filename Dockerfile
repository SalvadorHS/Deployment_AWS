FROM python:3.7
COPY . /home/Schrimp_app
WORKDIR /home/Schrimp_app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
