FROM python:3

ADD test.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

ENV FLASK_APP test.py

CMD [ "flask", "run",  "--host=0.0.0.0" ]