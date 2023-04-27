FROM python:3.9-slim

COPY ./requirements.txt /opt/app/requirements.txt
COPY ./domain /opt/app/domain
COPY ./controller /opt/app/controller
COPY ./repository /opt/app/repository
COPY ./service /opt/app/service

RUN pip install --no-cache-dir -r /opt/app/requirements.txt

ENTRYPOINT ["python", "/opt/app/controller/controller.py"]