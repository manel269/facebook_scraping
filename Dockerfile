FROM python:3.9.7



WORKDIR /
COPY "requirements.txt", "./"

RUN pip install --no-cache-dir uvicorn \
    && pip install -r requirements.txt 

EXPOSE 80
EXPOSE 443
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
