FROM python:3.10

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "nova/manage.py", "runserver", "0.0.0.0:8000"]