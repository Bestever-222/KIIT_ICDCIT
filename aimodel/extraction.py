import pdfplumber
import re
from pytesseract import image_to_string
from PIL import Image
import PyPDF2
import pdfplumber
import pandas as pd
import json
from ApiKey import get_groq_response

pdf_path = r"aimodel\blood_test_report.pdf"

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file using pdfplumber and remove duplicate lines.
    """
    unique_lines = set()  # Use a set to store unique lines
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.splitlines()  # Split text into individual lines
                unique_lines.update(lines)  # Add lines to the set (duplicates are automatically ignored)
    return "\n".join(sorted(unique_lines))  # Join the unique lines into a single string


def identify_report_type_with_groq(text):
    """
    Use the Groq API to identify the type of medical report from the text.
    """
    prompt = f"""
You are an intelligent assistant. Analyze the following text extracted from a medical report and tell me which report it is. 
Choose only one of the following options: 
"Blood Report," "Biopsy Report," "X-Ray Report," "MRI Report," "CT Scan Report," "Ultrasound Report," "Pathology Report," "ECG Report," "Dental Report," or "Unknown Report Type."

Give me just report name nothing else
Medical Report Text:
{text}

Report Type (choose one):
"""
    try:
        response = get_groq_response(prompt)
        return response.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    # Step 1: Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)
    # Step 2: Use Groq to identify the type of report
    report_type = identify_report_type_with_groq(text)
    return str(report_type)

if __name__ == "__main__":
    report_type = main()
    print(report_type)



type = report_type
path = pdf_path
# Dictionary of patterns for various reports
FIELD_PATTERNS = {
    "Blood Report": {
    "Hemoglobin": r"Hemoglobin[:\-]?\s*(\d+\.?\d*)",
    "Blood Sugar (Fasting)": r"Blood Sugar[:\-]?\s*(\d+\.?\d*)",
    "Blood Sugar (Postprandial)": r"Postprandial[:\-]?\s*(\d+\.?\d*)",
    "Cholesterol (Total)": r"Cholesterol[:\-]?\s*(\d+\.?\d*)",
    "LDL (Low-Density Lipoprotein)": r"LDL[:\-]?\s*(\d+\.?\d*)",
    "HDL (High-Density Lipoprotein)": r"HDL[:\-]?\s*(\d+\.?\d*)",
    "Triglycerides": r"Triglycerides[:\-]?\s*(\d+\.?\d*)",
    "RBC (Red Blood Cell Count)": r"RBC[:\-]?\s*(\d+\.?\d*)",
    "WBC (White Blood Cell Count)": r"WBC[:\-]?\s*(\d+\.?\d*)",
    "Platelets": r"Platelets[:\-]?\s*(\d+\.?\d*)",
    "Hematocrit (HCT)": r"Hematocrit[:\-]?\s*(\d+\.?\d*)",
    "MCV (Mean Corpuscular Volume)": r"MCV[:\-]?\s*(\d+\.?\d*)",
    "MCH (Mean Corpuscular Hemoglobin)": r"MCH[:\-]?\s*(\d+\.?\d*)",
    "MCHC (Mean Corpuscular Hemoglobin Concentration)": r"MCHC[:\-]?\s*(\d+\.?\d*)",
    "ESR (Erythrocyte Sedimentation Rate)": r"ESR[:\-]?\s*(\d+\.?\d*)",
    "C-Reactive Protein (CRP)": r"C-Reactive Protein[:\-]?\s*(\d+\.?\d*)",
    "Urea": r"Urea[:\-]?\s*(\d+\.?\d*)",
    "Creatinine": r"Creatinine[:\-]?\s*(\d+\.?\d*)",
    "Calcium": r"Calcium[:\-]?\s*(\d+\.?\d*)",
    "Potassium": r"Potassium[:\-]?\s*(\d+\.?\d*)",
    "Sodium": r"Sodium[:\-]?\s*(\d+\.?\d*)",
    "Albumin": r"Albumin[:\-]?\s*(\d+\.?\d*)",
    "Globulin": r"Globulin[:\-]?\s*(\d+\.?\d*)",
    "Bilirubin (Total)": r"Bilirubin[:\-]?\s*(\d+\.?\d*)",
    "Alkaline Phosphatase (ALP)": r"Alkaline Phosphatase[:\-]?\s*(\d+\.?\d*)",
    "SGPT (ALT)": r"SGPT[:\-]?\s*(\d+\.?\d*)",
    "SGOT (AST)": r"SGOT[:\-]?\s*(\d+\.?\d*)",
    "Vitamin D": r"Vitamin D[:\-]?\s*(\d+\.?\d*)",
    "Vitamin B12": r"Vitamin B12[:\-]?\s*(\d+\.?\d*)",
    "Iron": r"Iron[:\-]?\s*(\d+\.?\d*)",
    "Ferritin": r"Ferritin[:\-]?\s*(\d+\.?\d*)",
    "TSH (Thyroid-Stimulating Hormone)": r"TSH[:\-]?\s*(\d+\.?\d*)"
},
    "Biopsy": {
    "Tissue Source": r"Tissue Source[:\-]?\s*(.*)",
    "Clinical Diagnosis": r"Clinical Diagnosis[:\-]?\s*(.*)",
    "Pathological Diagnosis": r"Pathological Diagnosis[:\-]?\s*(.*)",
    "Histological Findings": r"Histological Findings[:\-]?\s*(.*)",
    "Immunohistochemistry Markers": r"Immunohistochemistry Markers[:\-]?\s*(.*)",
    "Grade of Tumor": r"Grade[:\-]?\s*(.*)",
    "Stage of Tumor": r"Stage[:\-]?\s*(.*)",
    "Margins": r"Margins[:\-]?\s*(.*)",
    "Lymphovascular Invasion": r"Lymphovascular Invasion[:\-]?\s*(.*)",
    "Perineural Invasion": r"Perineural Invasion[:\-]?\s*(.*)",
    "Mitotic Count": r"Mitotic Count[:\-]?\s*(.*)",
    "Comments": r"Comments[:\-]?\s*(.*)"
},

    "Urinalysis": {
    "Color": r"Color[:\-]?\s*(.*)",
    "Appearance": r"Appearance[:\-]?\s*(.*)",
    "Specific Gravity": r"Specific Gravity[:\-]?\s*(\d+\.?\d*)",
    "pH": r"pH[:\-]?\s*(\d+\.?\d*)",
    "Protein": r"Protein[:\-]?\s*(.*)",
    "Glucose": r"Glucose[:\-]?\s*(.*)",
    "Ketones": r"Ketones[:\-]?\s*(.*)",
    "Bilirubin": r"Bilirubin[:\-]?\s*(.*)",
    "Urobilinogen": r"Urobilinogen[:\-]?\s*(.*)",
    "Blood": r"Blood[:\-]?\s*(.*)",
    "Nitrite": r"Nitrite[:\-]?\s*(.*)",
    "Leukocytes": r"Leukocytes[:\-]?\s*(.*)",
    "RBC Count": r"RBC Count[:\-]?\s*(\d+\.?\d*)",
    "WBC Count": r"WBC Count[:\-]?\s*(\d+\.?\d*)",
    "Epithelial Cells": r"Epithelial Cells[:\-]?\s*(.*)",
    "Casts": r"Casts[:\-]?\s*(.*)",
    "Crystals": r"Crystals[:\-]?\s*(.*)",
    "Bacteria": r"Bacteria[:\-]?\s*(.*)",
    "Yeast": r"Yeast[:\-]?\s*(.*)",
    "Comments": r"Comments[:\-]?\s*(.*)"
},
    
}


# Extract text from a PDF
def extract_text_from_pdf(path):
    try:
        text = ""
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return ""


# Extract fields based on patterns
def extract_fields(type, text):
    if type not in FIELD_PATTERNS:
        print(f"Report type '{type}' not supported!")
        return {}

    fields = {}
    patterns = FIELD_PATTERNS[type]
    for field, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        fields[field] = match.group(1).strip() if match else "Not Found"
    return fields


# Process a report based on type and format
def process_report(file_path, file_type, type):
    if file_type == "pdf":
        text = extract_text_from_pdf(file_path)
    else:
        print("Unsupported file type!")
        return None

    if text:
        fields = extract_fields(type, text)
        print(f"Extracted Fields for {type}:")
        for key, value in fields.items():
            print(f"{key}: {value}")
        return fields
    else:
        print("No text extracted!")
        return None

def save_extracted_fields_to_json(fields, output_path="aimodel\extracted_fields.json"):
    """
    Save the extracted fields into a JSON file.
    """
    with open(output_path, "w") as json_file:
        json.dump(fields, json_file, indent=4)
    print(f"Fields saved to {output_path}")


if __name__ == "__main__":
    pdf_path = "aimodel\\blood_test_report.pdf"
    report_type = "Blood Report"  # Example, dynamically set this in your workflow
    text = extract_text_from_pdf(pdf_path)
    fields = extract_fields(report_type, text)

    # Save fields to a JSON file
    save_extracted_fields_to_json(fields)