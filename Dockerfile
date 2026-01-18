FROM python:3.9-slim
WORKDIR /app
COPY guardian.py .
CMD ["python", "guardian.py"]
