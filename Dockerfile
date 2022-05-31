FROM python:3.10

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./setup.py .

RUN pip install -e .

COPY . .

CMD [ "uvicorn", "main:app", "--port", "8000"]
