FROM python:3.11-alpine3.19
WORKDIR /app

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /app

EXPOSE 5000 
# uvicorn main:app --hsot 0.0.0.0 --port 5000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]