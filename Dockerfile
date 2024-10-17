# Use the official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /pesel_task

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Copy the application code
COPY . .
CMD ["python", "./pesel_task/manage.py", "runserver", "0.0.0.0:8000"]