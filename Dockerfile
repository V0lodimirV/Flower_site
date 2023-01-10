FROM python:3.10

COPY a_configuration/requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1


COPY a_configuration .

ENTRYPOINT [ "python", "manage.py", "runserver" ]