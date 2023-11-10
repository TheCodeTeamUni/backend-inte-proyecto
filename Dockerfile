# Pull official base image
FROM public.ecr.aws/docker/library/python:3.9-slim-buster

# Set work directory
WORKDIR /app

# Set enviroment variables
ENV USERS_PATH default
ENV ASPIRANTS_PATH default
ENV PROJECT_PATH default

# Install pip requirements
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN python -m pip install -r requirements.txt

# Copy Project
COPY . /app

# Expose port
EXPOSE 3000

CMD ["python3", "application.py"]