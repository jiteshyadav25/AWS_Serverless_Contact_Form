
const API_URL = "https://3ykoexz9c3.execute-api.us-east-1.amazonaws.com/contact";

document.getElementById("contactForm")
        .addEventListener("submit", async function(event) {

            event.preventDefault();

            const button =
                document.getElementById("submitBtn");

            const result =
                document.getElementById("result");

            const data = {
                name: document.getElementById("name").value,
                email: document.getElementById("email").value,
                message: document.getElementById("message").value
            };

            button.disabled = true;
            button.innerText = "Sending...";
            result.innerText = "";

            try {

                const response = await fetch(API_URL, {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify(data)
                });

                const output = await response.json();

                if (!response.ok) {
                    throw new Error(output.message);
                }

                result.innerText = output.message;
                result.style.color = "green";

                document.getElementById("contactForm").reset();

            } catch (error) {

                result.innerText =
                    error.message || "Something went wrong";

                result.style.color = "red";

            } finally {

                button.disabled = false;
                button.innerText = "Send Message";

            }

        });