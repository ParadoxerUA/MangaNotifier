FROM gcr.io/google-appengine/python

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

ADD requirements.txt /app/requirements.txt
ADD . /app

RUN apt-get update && apt-get upgrade -y && apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi -y
RUN virtualenv /env -p python3.7
RUN pip install -r /app/requirements.txt

CMD gunicorn -b :$PORT notifier.notifier.wsgi
