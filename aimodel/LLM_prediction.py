import json
from ApiKey import get_groq_response
import json
import re

def extract_valid_json(input_string):
    """
    Extract valid JSON from a string that may contain additional non-JSON content.

    Args:
        input_string (str): The input string potentially containing JSON.

    Returns:
        dict or None: The extracted JSON object as a Python dictionary, or None if extraction fails.
    """
    try:
        # Try to directly parse the input string as JSON
        return json.loads(input_string)
    except json.JSONDecodeError:
        # Attempt to extract JSON using regex
        json_pattern = re.compile(r'\{(?:[^{}]|(?R))*\}')
        match = json_pattern.search(input_string)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
    return None

def load_extracted_fields_from_json(input_path="aimodel\\extracted_fields.json"):
    """
    Load extracted fields from a JSON file.
    """
    with open(input_path, "r") as json_file:
        fields = json.load(json_file)
    return fields


def build_groq_prompt(fields):
    """
    Build a Groq prompt using the extracted fields.
    """
    field_summary = "\n".join(f"{key}: {value}" for key, value in fields.items())
    prompt = f"""
You are a specialized medical AI assistant trained to analyze patient data for detecting potential risks related to anemia, diabetes, tumors, and cancer. Based on the provided medical data, perform the following tasks:

Analyze the data to identify any indicators, patterns, or abnormalities that could suggest a risk of anemia, diabetes, tumors, or cancer.
Provide specific insights into the stage or severity of these conditions, if possible.
Recommend the most relevant diagnostic tests or evaluations to confirm the presence of these conditions.
Suggest preventive measures or early interventions if risks are identified.
while suggesting test only give neccessary test

Extracted Medical Data:
{field_summary}

Output Format (JSON):
{{
    "ConditionIdentified": {{
        "FeatureName": "Anemia/Diabetes/Tumor/Cancer/No risks detected",
        "Indicators": ["List of key data points supporting the finding"]
    }},
    "RecommendedTests": {{
        "Tests": ["name" :"Test names with reasons",
        "Time": "after how much time need to do the test"]
        
    }},
    "PreventiveMeasures": {{
        "Measures": ["Detailed suggestions for preventive or early intervention measures"]
    }}
}}
Respond strictly in JSON format without any additional explanation or text in feature name jsut keep any one of Anemia/Diabetes/Tumor/Cancer/No risks detected these.
it should strictly contain json only not even extra char. if no condition is identified then dont suggest any report just tell how to maintain the life style
"""
    return prompt


def save_response_to_json(response, output_path="aimodel\\groq_response.json"):
    """
    Save the Groq response to a JSON file.
    """
    # Check if response is already JSON-like
    try:
        # Parse the string response into JSON
        parsed_response = json.loads(response)
    except json.JSONDecodeError:
        print("Error: The response is not valid JSON.")
        return

    # Save the JSON response to the file
    with open(output_path, "w") as json_file:
        json.dump(parsed_response, json_file, indent=4)

    print(f"Response successfully saved to {output_path}.")



if __name__ == "__main__":
    # Load fields from JSON
    extracted_fields = load_extracted_fields_from_json()

    # Build the Groq prompt
    groq_prompt = build_groq_prompt(extracted_fields)

    # Get Groq response
    response = get_groq_response(groq_prompt)

    # Save the response to a JSON file
    save_response_to_json(response)

    # Print the response for verification
    print(response)
