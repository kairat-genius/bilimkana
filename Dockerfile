FROM python:3.12

RUN apt-get update && apt-get install -y \
    supervisor \
    && rm -rf /vat/lib/apt/lists/* \

WORKDIR /bilimsystem

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./*.sh

CMD [ "./app.sh" ]
