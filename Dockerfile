# Set the base image. 
FROM python:2.7
# Label for the Docker image
LABEL maintainer="Nikos Kordis"
# Copy files from the host to the container filesystem. 
COPY . /app
#  Set the working directory within the container
WORKDIR /app
# Install dependencies defined in the requirements.txt file. 
RUN pip install -r techtrends/requirements.txt
# Expose the application port
EXPOSE 3111
# Run on container start.
CMD [ "python", "techtrends/python init_db.py" ; "python", "techtrends/app.py"]