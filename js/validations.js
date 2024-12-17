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
    // Replace with backend API integration logic
    sendToBackend({ name, email, businessName, serviceRequired });
});

function sendToBackend(formData) {
    console.log('Form Data:', formData);
    // Placeholder for integration with AWS SES or backend server
}
