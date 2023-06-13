# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app.py file to the working directory
COPY app.py .

# Expose the default port for the Streamlit application
EXPOSE 8501

# Set the command to run when the container starts
CMD ["streamlit", "run", "app.py"]
