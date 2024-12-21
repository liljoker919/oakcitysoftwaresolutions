const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', async function (e) {
        e.preventDefault();
        const submitButton = contactForm.querySelector('button[type="submit"]');
        const loadingIndicator = document.getElementById('loadingIndicator');

        const name = document.getElementById('name').value.trim();
        const serviceRequired = document.getElementById('serviceRequired').value.trim();
        const businessName = document.getElementById('businessName').value.trim();
        const email = document.getElementById('email').value.trim();

        // Validate Name
        if (!name) {
            alert('Please enter your name.');
            return;
        }

        // Validate Email
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(email)) {
            alert('Please enter a valid email address.');
            return;
        }

        // Validate Service Required
        if (!serviceRequired) {
            alert('Please select a service.');
            return;
        }
        submitButton.disabled = true;
        loadingIndicator.textContent = 'Submitting...';
        loadingIndicator.classList.add('visible');
        alert('Form is valid! Submitting...');
        await sendToBackend({ name, email, businessName, serviceRequired }); // Call backend function
    });
}

async function sendToBackend(formData) {
    try {
        const response = await fetch('https://174ar5gms9.execute-api.us-east-1.amazonaws.com/prod', { // Replace with your API Gateway endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        const result = await response.json();
        if (response.ok) {
            console.log('Response:', result);
        } else {
            console.error('Error:', response.status, response.statusText, result);
            alert('Failed to send your message. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
        loadingIndicator.classList.remove('visible');
        submitButton.disabled = false;
        contactForm.removeChild(loadingIndicator);
    }
}

