from groq import Groq

# Initialize the Groq client
api_key = "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"  # Replace with your API key
client = Groq(api_key=api_key)

def get_groq_response(prompt):
    """
    Use Groq API to get a response.
    """
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.2-90b-vision-preview", 
            temperature=0.5,
            max_tokens=2000,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
