FROM python:3.10.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin \
    && apt-get install -y cron \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/list/*
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
