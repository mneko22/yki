FROM python:3.7-slim
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt
CMD ["python", "main.py", "--host=0.0.0.0", "--port=8080"]