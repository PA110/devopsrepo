
# Flask-MySQL CI/CD Pipeline

This project demonstrates a fully automated CI/CD pipeline using Jenkins, Docker, and AWS.

## Architecture
- **Front-end:** Python Flask
- **Back-end:** MySQL 8.0
- **Orchestration:** Docker Compose
- **CI/CD:** Jenkins (Pipeline as Code)
- **Infrastructure:** AWS EC2

## How to use
1. Push this code to your GitHub repo.
2. Setup Jenkins on your EC2 instance.
3. Point Jenkins to your repository `Jenkinsfile`.
4. Access the app at `http://your-ec2-ip:5000`.
