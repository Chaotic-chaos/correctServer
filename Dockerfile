FROM python:3.8-slim

MAINTAINER chaos:life0531@foxmail.com

RUN mkdir /root/correct_server

WORKDIR /root/correct_server

ADD . /root/correct_server

RUN pip3 install torch --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

CMD ["python3", "main.py"]
