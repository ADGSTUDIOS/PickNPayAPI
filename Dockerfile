FROM python:3.8 
LABEL maintainer="adgsenpai"

COPY . .

RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

