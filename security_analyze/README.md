# Code Security Analyzer

Code Security Analyzer is a comprehensive tool designed to analyze code files for potential vulnerabilities. It offers both a **web-based interface** and a **command-line interface (CLI)**, making it accessible for developers with different workflows. The project leverages a **pre-trained machine learning model** to detect vulnerabilities and provide actionable recommendations for fixing them. Additionally, it generates detailed security reports in PDF format.

[![Demo Video](https://img.shields.io/badge/Demo-Video-blue)](https://your-demo-video-url.com)

---

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
  - [Pre-trained Model](#pre-trained-model)
  - [Capabilities and Limitations](#capabilities-and-limitations)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Web Mode](#web-mode)
  - [CLI Mode](#cli-mode)
  - [REST API](#rest-api)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Web Mode**:
  - Upload code files via a user-friendly web interface.
  - Analyze code for vulnerabilities and display results dynamically.
  - Dark mode support for better user experience.
  - Displays recommended fixes for detected vulnerabilities.
  - Responsive design optimized for various devices.

- **CLI Mode**:
  - Analyze code files directly from the command line.
  - Output results in a structured format (e.g., JSON or plain text).
  - Ideal for developers who prefer terminal-based workflows.

- **REST API**:
  - Exposes an API endpoint for programmatic analysis of code.
  - Accepts JSON payloads with code and language information.
  - Returns predictions and recommended fixes.

- **Pre-trained Model**:
  - Utilizes a machine learning model trained on a dataset of secure and insecure code patterns.
  - Capable of detecting common vulnerabilities like SQL injection, XSS, and insecure file handling.

- **Dynamic Results**:
  - Provides detailed analysis results, including:
    - Vulnerability type.
    - Code snippet causing the issue.
    - Recommended fixes.

- **File Type Support**:
  - Supports multiple programming languages, including Python, JavaScript, C, Java, and PHP.

- **Security Report Generation**:
  - Generates a PDF report summarizing the analysis results.

---

## How It Works

### Pre-trained Model

The project uses a **pre-trained machine learning model** based on the `CodeBERTa` architecture. The model was fine-tuned on a dataset of secure and insecure code snippets, annotated with vulnerability types. Here's how it works:

1. **Input Processing**:
   - The uploaded or provided code file is tokenized and preprocessed into a format suitable for the model.
   
2. **Vulnerability Detection**:
   - The model analyzes the code for patterns associated with vulnerabilities.
   - It assigns a probability score to each detected issue.

3. **Recommendation Generation**:
   - Based on the detected vulnerabilities, the system generates recommendations for fixing the issues.

#### Model Details:
- **Architecture**: CodeBERTa (based on RoBERTa).
- **Training Dataset**: A curated dataset of 50,000+ secure and insecure code snippets.
- **Framework**: Hugging Face Transformers (PyTorch).
- **Limitations**:
  - The model is not perfect and may produce false positives or miss certain vulnerabilities.
  - It works best with common programming languages like Python, JavaScript, C, Java, and PHP.

---

### Capabilities and Limitations

#### What the Project Can Do:
- Detect common vulnerabilities in code files.
- Provide recommendations for fixing detected issues.
- Support both web and CLI modes for flexibility.
- Analyze multiple programming languages.
- Generate PDF reports summarizing the analysis.

#### What the Project Cannot Do:
- Detect highly complex or obscure vulnerabilities.
- Guarantee 100% accuracy in analysis.
- Replace manual code reviews by security experts.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Hugging Face Transformers (CodeBERTa)
- **Database**: SQLite
- **PDF Generation**: ReportLab
- **Template Engine**: Jinja2
- **Styling**: Custom CSS
- **JavaScript Features**: LocalStorage for dark mode, dynamic animations
- **Testing**: Pytest (for backend testing)

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/code-security-analyzer.git
   cd code-security-analyzer
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Pre-trained Model**:
   - Download the model file from [this link](https://your-model-download-link.com).
   - Place the model file in the `models/` directory.

5. **Run the Application**:
   ```bash
   flask run
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Project Structure

```
security_analyze/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
├── templates/
│   └── index.html
├── models/
│   └── vulnerability_model.h5
├── uploads/
│   ├── example.c
│   ├── example.py
├── app.py
├── analyze.py
├── test_analyze.py
├── analysis_results.db
├── requirements.txt
└── README.md
```

- **`static/`**: Contains static assets like CSS and JavaScript files.
- **`templates/`**: Contains HTML templates for the web interface.
- **`models/`**: Contains the pre-trained machine learning model.
- **`uploads/`**: Stores uploaded files for analysis.
- **`app.py`**: The main Flask application file for the web interface.
- **`analyze.py`**: Contains the core logic for analyzing code and generating reports.
- **`test_analyze.py`**: Contains test cases for the application.
- **`analysis_results.db`**: SQLite database for storing analysis results.
- **`requirements.txt`**: Lists the Python dependencies.

---

## Usage

### Web Mode

1. Open the application in your browser.
2. Upload a code file using the provided form.
3. Click the "Analyze" button to start the security analysis.
4. View the results, including any detected vulnerabilities and recommended fixes.

### CLI Mode

1. Run the CLI tool with the following command:
   ```bash
   python analyze.py --cli
   ```
2. Follow the interactive prompts to analyze code snippets or files.

### REST API

1. Use the `/api/analyze` endpoint to analyze code programmatically.
2. Send a POST request with the following JSON payload:
   ```json
   {
       "code": "your code snippet here",
       "language": "python"
   }
   ```
3. Receive a response with the prediction and recommended fixes.

---

## Testing

To run the tests, use the following command:

```bash
pytest
```

This will execute all test cases in the `test_analyze.py` file to ensure the application is functioning correctly.

---

## Future Enhancements

- **Support for Additional Languages**: Extend support to analyze more programming languages.
- **Detailed Reports**: Generate downloadable reports for the analysis results.
- **Real-Time Analysis**: Provide real-time feedback as the user uploads the file.
- **User Authentication**: Add user accounts to save analysis history.
- **Improved Model Accuracy**: Train the model on a larger and more diverse dataset.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

---

## Acknowledgments

- **CS50**: For inspiring this project.
- **Flask Documentation**: For providing excellent resources.
- **Hugging Face**: For enabling the use of CodeBERTa.
- **Open Source Libraries**: For making development easier.

---

Feel free to reach out if you have any questions or suggestions!
