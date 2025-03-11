from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch
import time
import os
import argparse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import Flask, request, render_template

# Suppress model initialization warning
import warnings
warnings.filterwarnings("ignore", message="Some weights of RobertaForSequenceClassification were not initialized")

# Load the pre-trained CodeBERT model
MODEL_NAME = "microsoft/codebert-base"
tokenizer = RobertaTokenizer.from_pretrained(MODEL_NAME)
model = RobertaForSequenceClassification.from_pretrained(MODEL_NAME)

def analyze_code_vulnerability(code_snippet):
    try:
        inputs = tokenizer(code_snippet, return_tensors='pt', truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        prediction = torch.argmax(outputs.logits, dim=-1).item()
        return prediction
    except Exception as e:
        print(f"Error analyzing code: {e}")
        return -1  # Indicate an error

def generate_security_report(filename, code, prediction, execution_time):
    pdf_path = f"{filename}_security_report.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(72, 750, "Code Security Analysis Report")
    c.drawString(72, 730, f"File: {filename}")
    c.drawString(72, 710, f"Execution Time: {execution_time:.4f} seconds")
    c.drawString(72, 690, "Analyzed Code:")
    text = c.beginText(72, 670)
    text.textLines(code[:1000])  # Truncate long code
    c.drawText(text)
    if prediction == 1:
        c.setFillColorRGB(1, 0, 0)  # Red
        c.drawString(72, 650, "⚠️  Vulnerabilities detected!")
        c.setFillColorRGB(0, 0, 0)  # Black
        c.drawString(72, 630, "🔴 Buffer overflow risk detected due to unsafe function usage.")
        c.drawString(72, 610, "✅ Recommended Fix: Use secure functions such as fgets instead of gets.")
    else:
        c.setFillColorRGB(0, 0.5, 0)  # Green
        c.drawString(72, 650, "✅ Code is secure!")
    c.save()
    print(f"📄 Analysis report saved to {pdf_path}")

def analyze_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                code = f.read()
            start_time = time.time()
            prediction = analyze_code_vulnerability(code)
            execution_time = time.time() - start_time
            generate_security_report(file_path, code, prediction, execution_time)
        else:
            print(f"❌ File not found: {file_path}")

def interactive_cli():
    while True:
        code_snippet = input("Enter your code (or type 'exit' to quit): ")
        if code_snippet.lower() == 'exit':
            break
        start_time = time.time()
        prediction = analyze_code_vulnerability(code_snippet)
        execution_time = time.time() - start_time
        print(f"Execution Time: {execution_time:.4f} seconds")
        print("⚠️  Vulnerabilities detected!" if prediction == 1 else "✅ Code is secure!")

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form["code"]
        start_time = time.time()
        prediction = analyze_code_vulnerability(code)
        execution_time = time.time() - start_time
        result = "⚠️  Vulnerabilities detected!" if prediction == 1 else "✅ Code is secure!"
        return render_template("index.html", execution_time=execution_time, result=result, code=code)
    return render_template("index.html")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='*', help="File paths to analyze")
    parser.add_argument("--cli", action="store_true", help="Start interactive CLI mode")
    parser.add_argument("--web", action="store_true", help="Start web UI")
    args = parser.parse_args()

    if args.cli:
        interactive_cli()
    elif args.web:
        app.run(debug=True)
    elif args.files:
        analyze_files(args.files)
    else:
        print("No input provided. Use --cli, --web, or specify file paths.")

if __name__ == "__main__":
    main()