FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# create root directory for our project in the container
RUN mkdir /code


# Set the working directory to /code
WORKDIR /code
# Copy the current directory contents into the container at /code
COPY . /code/

# installs and upgrades the pip version that is in the container.
RUN pip install --upgrade pip


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000