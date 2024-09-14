FROM python:3.12

WORKDIR /opt/TeleBtProjectDocker
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /img1 .
COPY /tags1 .

COPY main.py .
CMD ["python3", "main.py"]