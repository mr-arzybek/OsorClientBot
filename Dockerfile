FROM python:3.10
EXPOSE 5002
RUN mkdir -p /opt/osor_client_bot
WORKDIR /opt/osor_client_bot

RUN mkdir -p /opt/osor_client_bot/requirements
ADD requirements.txt /opt/osor_client_bot/

COPY . /opt/osor_client_bot/

RUN pip install -r requirements.txt
CMD ["python", "/opt/osor_client_bot/main.py"]