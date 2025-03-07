document
  .getElementById("login-form")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    // Clear previous error messages
    clearErrors();

    // Get form values
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    let isValid = true;

    // Validate email
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
      displayError("email", "Please enter a valid email");
      isValid = false;
    }

    // Validate password
    if (password === "") {
      displayError("password", "Password is required");
      isValid = false;
    }

    // If everything is valid, you can submit the form or send data to the server
    if (isValid) {
      alert("Login successful!");
      // Here you can submit the form data or redirect to another page
    }
  });

// Function to display error messages
function displayError(field, message) {
  const errorElement = document.getElementById(`${field}-error`);
  errorElement.textContent = message;
}
