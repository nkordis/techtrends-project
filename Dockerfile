# Set the base image
FROM python:2.7
# Label for the Docker image
LABEL maintainer="Nikos Kordis"
# Copy files from host to the container filesystem
COPY /techtrends /app
#  Set the working directory within the container
WORKDIR /app
# Install dependencies defined in requirements.txt file
RUN pip install -r requirements.txt
# Run the database script
RUN python init_db.py
# Expose the container port
EXPOSE 3111
# Run on container start
CMD ["python", "app.py"]