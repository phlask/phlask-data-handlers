# Docker
FROM python:3.10.9

WORKDIR /dashboard

# copy the dependencies from the requirements.txt file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt


# Copy the Flask application code to the working directory
COPY app.py .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Run the Flask development server
CMD ["flask", "run", "--host=0.0.0.0"]