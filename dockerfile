FROM python:3.11

RUN mkdir test

WORKDIR test

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD pytest -v test.py