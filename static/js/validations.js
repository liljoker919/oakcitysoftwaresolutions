document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("contactForm");
    if (contactForm) {
        contactForm.addEventListener("submit", async function (e) {
            e.preventDefault();

            const submitButton = contactForm.querySelector('button[type="submit"]');
            const loadingIndicator = document.getElementById("loadingIndicator");

            const name = document.getElementById("name").value.trim();
            const serviceRequired = document.getElementById("serviceRequired").value.trim();
            const businessName = document.getElementById("businessName").value.trim();
            const email = document.getElementById("email").value.trim();

            // Validate Name
            if (!name) {
                alert("Please enter your name.");
                return;
            }

            // Validate Email
            const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (!emailRegex.test(email)) {
                alert("Please enter a valid email address.");
                return;
            }

            // Validate Service Required
            if (!serviceRequired) {
                alert("Please select a service.");
                return;
            }

            // Disable submit button and show loading indicator
            submitButton.disabled = true;
            if (loadingIndicator) {
                loadingIndicator.textContent = "Submitting...";
                loadingIndicator.classList.add("visible");
            }

            try {
                // Send data to backend
                const response = await sendToBackend({ name, email, businessName, serviceRequired });

                if (response.ok) {
                    const result = await response.json();
                    console.log("Response:", result);
                    alert("Your message has been sent successfully!");
                } else {
                    console.error("Error:", response.status, response.statusText);
                    alert("Failed to send your message. Please try again.");
                }
            } catch (error) {
                console.error("Error:", error);
                alert("An error occurred. Please try again later.");
            } finally {
                // Reset form and button states
                submitButton.disabled = false;
                if (loadingIndicator) {
                    loadingIndicator.classList.remove("visible");
                    loadingIndicator.textContent = "";
                }
            }
        });
    }
});

async function sendToBackend(formData) {
    try {
        const response = await fetch('https://174ar5gms9.execute-api.us-east-1.amazonaws.com/prod', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        // Handle non-JSON responses gracefully
        let result;
        try {
            result = await response.json();
        } catch (jsonError) {
            console.error('Failed to parse JSON response:', jsonError);
            throw new Error('Invalid server response');
        }

        if (response.ok) {
            console.log('Response:', result);
            alert('Your message has been sent successfully!');
        } else {
            console.error('Server returned an error:', response.status, response.statusText, result);
            alert(`Failed to send your message: ${result.message || 'Unknown error occurred'}`);
        }
    } catch (error) {
        console.error('Error occurred during submission:', error);
        alert('An error occurred. Please try again later.');
    }
}

