FROM python:3.9.0

COPY sample.py requirements.txt ./

RUN pip install -r requirements.txt --no-cache

CMD ["python", "sample.py"]