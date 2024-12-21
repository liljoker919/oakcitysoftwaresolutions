document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const businessName = document.getElementById('businessName').value.trim();
    const serviceRequired = document.getElementById('serviceRequired').value;

    // Validate Name
    if (!name) {
        alert('Please enter your name.');
        return;
    }

    // Validate Email
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    // Validate Service Required
    if (!serviceRequired) {
        alert('Please select a service.');
        return;
    }

    alert('Form is valid! Submitting...');
    sendToBackend({ name, email, businessName, serviceRequired }); // Call backend function
});

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
            alert('Your message has been sent successfully!');
        } else {
            console.error('Error:', result);
            alert('Failed to send your message. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
    }
}
