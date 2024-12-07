// Global variable to store the input
let savedInput = "";

// Function to save the input and send it via a GET request
function saveAndSendInput() {
    // Step 1: Get the input value from the text box
    savedInput = document.getElementById("userInput").value;

    // Step 2: Provide feedback to the user
    document.getElementById("output").innerText = `You entered: ${savedInput}`;

    // Step 3: Build the GET request URL with query parameters
    const apiEndpoint = "/127.0.0.1:5000/fetchfiles/" + savedInput; // Replace with your API URL
    const urlWithParams = `${apiEndpoint}?input=${encodeURIComponent(savedInput)}`;

    // Step 4: Send the GET request
    fetch(urlWithParams, {
        method: "GET" // HTTP GET method
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        return response.json(); // Convert response to JSON
    })
    .then(data => {
        // Step 5: Handle API response
        console.log("API Response:", data);
        document.getElementById("output").innerText = "Input sent successfully!";
    })
    .catch(error => {
        console.error("Error sending data to API:", error);
        document.getElementById("output").innerText = "Failed to send input!";
    });
}