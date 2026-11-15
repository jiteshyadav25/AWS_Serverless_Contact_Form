import json
import os
import boto3
import re

ses = boto3.client(
    "ses",
    region_name=os.environ.get("AWS_REGION_NAME", "us-east-1")
)

SENDER_EMAIL = os.environ["SENDER_EMAIL"]
RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]


def response(status_code, message):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": message})
    }


def lambda_handler(event, context):

    try:
        # Read incoming request
        body = json.loads(event.get("body") or "{}")

        name = body.get("name", "").strip()
        email = body.get("email", "").strip()
        message = body.get("message", "").strip()

        # Validate form
        if not name or not email or not message:
            return response(400, "All fields are required")

        if len(name) > 100 or len(email) > 254 or len(message) > 5000:
            return response(400, "Input is too long")

        if not re.fullmatch(
            r"[^@\s]+@[^@\s]+\.[^@\s]+", email
        ):
            return response(400, "Invalid email address")

        # Send email through Amazon SES
        ses.send_email(
            Source=SENDER_EMAIL,
            Destination={
                "ToAddresses": [RECEIVER_EMAIL]
            },
            Message={
                "Subject": {
                    "Data": "New Contact Form Message"
                },
                "Body": {
                    "Text": {
                        "Data": (
                            f"Name: {name}\n"
                            f"Email: {email}\n"
                            f"Message: {message}"
                        )
                    }
                }
            },
            ReplyToAddresses=[email]
        )

        return response(
            200,
            "Your message has been sent successfully!"
        )

    except json.JSONDecodeError:
        return response(400, "Invalid JSON request")

    except Exception as e:
        print("Error:", str(e))
        return response(500, "Unable to send your message")
