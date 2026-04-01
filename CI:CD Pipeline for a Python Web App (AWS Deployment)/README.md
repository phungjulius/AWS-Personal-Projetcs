# CI/CD Pipeline Demo (AWS + GitHub Actions)

## Overview
This project demonstrates a simple CI/CD pipeline for deploying a Python web application to an AWS EC2 instance using GitHub Actions.

The pipeline automatically tests and deploys the application whenever changes are pushed to the main branch.

## Architecture
- Python Flask application
- GitHub Actions for CI/CD
- AWS EC2 for hosting

## Technologies
- Python (Flask)
- GitHub Actions
- AWS EC2
- Bash scripting

## CI/CD Workflow
1. Code is pushed to GitHub
2. GitHub Actions pipeline is triggered
3. Dependencies are installed
4. Tests are executed
5. If tests pass, the app is deployed to EC2 via SSH

## Deployment
The application runs on an EC2 instance and is accessible via:
http://<EC2-PUBLIC-IP>:5000

## Project Structure
- `app/` → Application code
- `tests/` → Unit tests
- `scripts/` → Deployment script
- `.github/workflows/` → CI/CD pipeline

## What I Learned
- Setting up CI/CD pipelines using GitHub Actions
- Automating deployment to cloud environments
- Managing application lifecycle in a simple production-like setup
- Debugging pipeline and deployment issues

## Future Improvements
- Use Docker for containerization
- Add HTTPS and domain configuration
- Use Infrastructure as Code (Terraform)