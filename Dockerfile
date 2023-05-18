FROM python:3.10-slim
RUN apt update && \
    apt upgrade -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
CMD [ "bash" ]