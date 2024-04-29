FROM python:3.12

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY *.py /app

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "testorigin:app", "--host", "0.0.0.0", "--port", "80"]


