FROM python:3.7-alpine
WORKDIR /code
COPY . .
RUN pip install flask redis
CMD ["python", "app.py"]
