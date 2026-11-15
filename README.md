# ☁️ AWS Serverless Contact Form 📩

### 🚀 A serverless contact form built using AWS cloud services

Welcome to my AWS Serverless Contact Form project!

I created this project to gain practical experience with AWS and understand how different cloud services work together to build a real-world application.

The website allows visitors to submit their name, email address, and message. The backend processes the information and sends the message to the receiver's email using Amazon SES — without managing a traditional server.

---

## 🌐 Live Website

👉 [Click here to visit my Contact Form](http://jitesh-serverless-contact-form.s3-website-us-east-1.amazonaws.com)

---

## 🖼️ Project Architecture & Preview

![AWS Serverless Contact Form Architecture](images/aws-serverless-contact-form.png)

---

## 🛠️ AWS Services Used

| AWS Service | Purpose |
|---|---|
| 🪣 Amazon S3 | Hosts the frontend website |
| 🌐 API Gateway | Receives contact form requests |
| ⚡ AWS Lambda | Processes form submissions |
| 📧 Amazon SES | Sends email notifications |
| 🔐 AWS IAM | Manages permissions and access |
| 📊 Amazon CloudWatch | Monitors Lambda logs and errors |

---

## 🔄 How Does It Work?

1. 👤 A visitor opens the contact form website.
2. ✍️ The visitor enters their name, email, and message.
3. 🌐 JavaScript sends the information to API Gateway.
4. ⚡ API Gateway triggers the Lambda function.
5. 🐍 Lambda validates the submitted information.
6. 📧 Amazon SES sends the message to the receiver's email.
7. ✅ The visitor receives a success or error response.

---

## ✨ Key Features

- 📱 Responsive contact form design
- ☁️ Serverless cloud architecture
- 📧 Email notifications using Amazon SES
- 🔐 IAM-based permissions
- ✅ Backend input validation
- 📊 CloudWatch logging
- 🚀 Static website hosting with Amazon S3

---

## 💻 Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- Amazon Web Services (AWS)

---

## 📂 Project Structure

```text
aws-serverless-contact-form/
│
├── index.html
├── style.css
├── script.js
├── README.md
│
└── images/
    └── aws-serverless-contact-form.png
```

---

## 🎓 What I Learned

Building this project helped me understand:

- How to host a static website using Amazon S3.
- How to create APIs using API Gateway.
- How to write and deploy Python Lambda functions.
- How to send emails using Amazon SES.
- How to configure IAM roles and permissions.
- How to configure CORS between frontend and backend.
- How to troubleshoot AWS deployment issues.
- How serverless architecture works in real-world applications.

---

## 🔮 Future Improvements

I would like to improve this project by adding:

- 🔒 HTTPS using Amazon CloudFront
- 🗄️ Amazon DynamoDB for storing messages
- 🛡️ Better spam protection
- 🎨 Improved user interface
- 📈 Better monitoring and error handling

---

## 👨‍💻 About Me

**Jitesh Yadav**

☁️ Aspiring Cloud & DevOps Engineer

I'm learning AWS, Linux, Python, networking, and DevOps through hands-on projects.

I believe the best way to learn cloud computing is by building real-world projects and solving practical problems.

---

⭐ If you find this project interesting, feel free to explore the repository!

**Thanks for visiting! 🙌**
