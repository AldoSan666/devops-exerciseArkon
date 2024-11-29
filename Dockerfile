
FROM python:3.9-slim
WORKDIR /app
COPY requirement.txt requirement.txt
COPY app.py .
COPY . . 
COPY "requirement.txt" .
RUN pip install -r requirement.txt
EXPOSE 5000
CMD ["python","app.py"]
