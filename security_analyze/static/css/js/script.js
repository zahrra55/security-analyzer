document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const fileInput = document.querySelector("input[type='file']");
    const resultsContainer = document.querySelector(".results-container");
    const loadingSpinner = document.createElement("div");

    // Create a loading spinner
    loadingSpinner.classList.add("loading-spinner");
    loadingSpinner.innerHTML = `
        <div class="spinner"></div>
        <p>Analyzing your file, please wait...</p>
    `;
    loadingSpinner.style.display = "none";
    document.body.appendChild(loadingSpinner);

    // Form submission handler
    form.addEventListener("submit", (e) => {
        e.preventDefault();

        // Validate file input
        if (!fileInput.files.length) {
            alert("Please select a file to analyze.");
            return;
        }

        // Show loading spinner
        loadingSpinner.style.display = "flex";

        // Simulate file analysis (replace this with actual form submission logic)
        setTimeout(() => {
            loadingSpinner.style.display = "none";

            // Simulate dynamic results (this will be replaced by server response)
            const isSecure = Math.random() > 0.5; // Randomly simulate secure/insecure results
            resultsContainer.innerHTML = `
                <h2>Analysis Result</h2>
                ${
                    isSecure
                        ? '<p class="success">✅ Code is secure!</p>'
                        : '<p class="warning">⚠️ Vulnerabilities detected!</p><pre class="fix">Suggested Fix: Replace unsafe code with secure alternatives.</pre>'
                }
            `;

            // Smooth scroll to results
            resultsContainer.scrollIntoView({ behavior: "smooth" });
        }, 2000); // Simulate a 2-second delay
    });
});