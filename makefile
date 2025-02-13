# Include environment variables
include .env
export

# Define variables for convenience
IMAGE_NAME = flask-bmi-bmr
PORT = 5000

# Declare the PHONY targets
.PHONY: init run test build clean

# Initialize dependencies (install Python packages)
init:
	@echo "Installing dependencies..."
	@pip install -r requirements.txt

# Run the Flask application
run:
	@echo "Running the Flask app on port $(PORT)..."
	@python app.py

# Run tests (Placeholder for now)
test:
	@echo "Running tests..."
	# Add your test command here (e.g., pytest)

# Build the Docker image
build:
	@echo "Building the Docker image $(IMAGE_NAME)..."
	@docker build -t $(IMAGE_NAME) .

# Clean up Docker containers and images
clean:
	@echo "Cleaning up Docker containers and images..."
	@docker rm -f $$(docker ps -a -q) || true
	@docker rmi -f $(IMAGE_NAME) || true
