# Health Calculator Service

## Description

The **Health Calculator Microservice** is a Python application that provides health-related calculations, including Body Mass Index (BMI) and Basal Metabolic Rate (BMR), via a RESTful API. This service is containerized using Docker and deployed on Azure App Service with a CI/CD pipeline managed by GitHub Actions.

## Architecture

```plaintext
.
├── .github
|   └── workflows
|       └── ci-cd.yml   
├── app.py
├── Dockerfile
├── health_utils.py
├── makefile
├── README.md
├── requirements.txt
└── test.py
```

## Features

- **Health Check**:  
  - **Endpoint**: `/health`  
  - **Method**: `GET`
  - **Output**: Status of the Health Calculator Service


- **BMI Calculation**:  
  - **Endpoint**: `/bmi`  
  - **Method**: `POST`  
  - **Input**: JSON containing `height` (in meters) and `weight` (in kilograms)  
  - **Output**: Calculated BMI rounded to two decimal places

- **BMR Calculation**:  
  - **Endpoint**: `/bmr`  
  - **Method**: `POST`  
  - **Input**: JSON containing `height` (in meters), `weight` (in kilograms), `age` (in years), and `gender` (`male` or `female`)  
  - **Output**: Calculated BMR rounded to two decimal places

## Secrets

- **TOKEN** : To push and pull the docker image in the private registry
- **AZURE_WEBAPP_PUBLISH_PROFILE** : Allow github actions to deploy the app in Azure