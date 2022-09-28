FROM continuumio/anaconda3
COPY . /home/Schrimp_app
WORKDIR /home/Schrimp_app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app