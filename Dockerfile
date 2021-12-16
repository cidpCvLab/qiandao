FROM python:3.8.12-slim-buster
WORKDIR /qiandao
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python3", "/qiandao/server.py"]