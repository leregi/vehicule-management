FROM python:3.9

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt 
COPY . /usr/src/app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

COPY ./app /usr/src/app

CMD [ "fastapi", "run", "app/main.py", "--port", "80", "--reload" ]
