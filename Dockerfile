FROM python:3

WORKDIR /home/app

ADD . /home/app

RUN pip install -r requirements.txt

ENV FLASK_APP test.py

CMD [ "flask", "run",  "--host=0.0.0.0" ]

EXPOSE 5000