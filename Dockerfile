FROM continuumio/anaconda3
COPY . /home/Schrimp_app
WORKDIR /home/Schrimp_app
EXPOSE 8000

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3","app.py"]