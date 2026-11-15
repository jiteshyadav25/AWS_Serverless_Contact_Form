# ☁️ AWS Serverless Contact Form with Email Notifications

A serverless web application built using AWS services to collect contact and job application details and deliver them directly to an email inbox.

## 🚀 Project Overview

This project demonstrates how to build and deploy a serverless web application using Amazon Web Services (AWS).

The application provides a professional and responsive contact form where users can submit their personal and professional information.

The submitted information is processed by an AWS Lambda function through Amazon API Gateway and delivered to the receiver's email using Amazon Simple Email Service (SES).

The application uses a serverless architecture, eliminating the need to manage traditional servers.

## 🌐 Live Demo

**Website:** [AWS Serverless Contact Form](http://jitesh-serverless-contact-form.s3-website-us-east-1.amazonaws.com)

## 🛠️ AWS Services & Technologies

| Service / Technology | Purpose |
|---|---|
| Amazon S3 | Hosts the static frontend website |
| Amazon API Gateway | Receives HTTP requests |
| AWS Lambda | Processes form submissions |
| Amazon SES | Sends email notifications |
| AWS IAM | Manages permissions and access |
| Amazon CloudWatch | Monitors execution logs and errors |
| Python | Backend programming |
| HTML5 & CSS3 | Frontend development |
| JavaScript | API integration |

## 🏗️ Project Architecture

**Application Workflow:**

Frontend (HTML, CSS, JavaScript) → Amazon S3 → API Gateway → AWS Lambda → Amazon SES → Email Inbox

![AWS Serverless Architecture](images/aws-serverless-contact-form.png)

## 🔄 How the Application Works

1. A user visits the contact form hosted on Amazon S3.
2. The user enters the required information.
3. JavaScript collects the submitted form data.
4. API Gateway receives the HTTP POST request.
5. AWS Lambda processes and validates the submitted information.
6. Amazon SES sends an email notification to the receiver.
7. The application returns a success or error response to the frontend.

## 📋 Contact Form Fields

The application collects the following information:

- Full Name
- Email Address
- Phone Number
- Job Title
- Total Experience
- Expected Salary
- Description About You

## ✨ Key Features

- Professional and responsive user interface.
- Simple and user-friendly contact form.
- Serverless backend architecture.
- Email notifications using Amazon SES.
- API integration using Amazon API Gateway.
- Backend processing with Python and AWS Lambda.
- IAM-based access control.
- Input validation and error handling.
- CloudWatch logging and monitoring.
- Static website hosting using Amazon S3.

## 📂 Project Structure

```text
aws-serverless-contact-form/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   └── lambda_function.py
│
├── images/
│   └── aws-serverless-contact-form.png
│
├── screenshots/
│
├── .gitignore
└── README.md
```

## 🔐 Security & Permissions

- Configured IAM execution roles for AWS Lambda.
- Applied permissions for Amazon SES email delivery.
- Used environment variables for application configuration.
- Implemented backend input validation.
- Avoided storing AWS credentials in source code.

## 🎓 Skills & Knowledge Gained

Through this hands-on project, I gained practical experience in:

- Understanding serverless computing.
- Deploying static websites using Amazon S3.
- Creating HTTP APIs using API Gateway.
- Developing Python-based Lambda functions.
- Integrating Amazon SES for email notifications.
- Configuring IAM roles and policies.
- Understanding event-driven architecture.
- Configuring CORS for frontend and backend communication.
- Monitoring application execution using CloudWatch.
- Troubleshooting AWS deployment and integration issues.
- Managing source code using Git and GitHub.

## 🔮 Future Enhancements

- Configure HTTPS using Amazon CloudFront.
- Store submitted contact information using Amazon DynamoDB.
- Implement CAPTCHA for spam protection.
- Improve frontend user experience.
- Configure CloudWatch alarms and monitoring.
- Add stronger request validation and API throttling.

## 👨‍💻 About Me

**Jitesh Yadav**

Aspiring Cloud & DevOps Engineer

I am passionate about cloud computing, AWS, Linux, Python, networking, and DevOps technologies.

I enjoy building hands-on projects to develop practical technical skills and understand how cloud infrastructure works in real-world applications.

**My goal is to build scalable, secure, and reliable cloud-based solutions.**

## 🔗 Connect & Explore

- GitHub: [Your GitHub Profile](https://github.com/YOUR_USERNAME)
- Project Repository: [AWS Serverless Contact Form](https://github.com/YOUR_USERNAME/aws-serverless-contact-form)

---

⭐ If you find this project useful, consider giving the repository a star!

**Thank you for visiting my project!**
