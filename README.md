# Code Security Analyzer

Code Security Analyzer is a web-based application designed to analyze uploaded code files for potential vulnerabilities. It provides users with a simple interface to upload files, performs security analysis on the code, and displays the results along with recommendations for fixing any detected issues.
  
## Features

- **File Upload**: Users can upload code files for analysis.
- **Security Analysis**: The application scans the uploaded code for vulnerabilities.
- **Dark Mode Support**: Automatically applies dark mode if enabled in the user's browser.
- **Dynamic Results**: Displays analysis results dynamically, including recommendations for fixing vulnerabilities.
- **Responsive Design**: Optimized for various screen sizes and devices.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Template Engine**: Jinja2
- **Styling**: Custom CSS
- **JavaScript Features**: LocalStorage for dark mode, dynamic animations
- **Testing**: Pytest (for backend testing)

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

4. **Run the Application**:
   ```bash
   flask run
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Open the application in your browser.
2. Upload a code file using the provided form.
3. Click the "Analyze" button to start the security analysis.
4. View the results, including any detected vulnerabilities and recommended fixes.

## Testing

To run the tests, use the following command:

```bash
pytest
```

This will execute all test cases in the `test_analyze.py` file to ensure the application is functioning correctly.

## Future Enhancements

- **Support for Multiple File Types**: Extend support to analyze more programming languages.
- **Detailed Reports**: Generate downloadable reports for the analysis results.
- **Real-Time Analysis**: Provide real-time feedback as the user uploads the file.
- **User Authentication**: Add user accounts to save analysis history.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **CS50**: For inspiring this project.
- **Flask Documentation**: For providing excellent resources.
- **Open Source Libraries**: For making development easier.

---

Feel free to reach out if you have any questions or suggestions!
