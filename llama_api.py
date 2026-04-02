import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def clean_output(text):
    lines = text.split("\n")
    
    cleaned = []
    for line in lines:
        if "Explanation" in line or "Time Complexity" in line:
            continue
        cleaned.append(line)
    
    return "\n".join(cleaned)

def generate_code(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a strict coding assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        raw_output = response.choices[0].message.content
        return clean_output(raw_output)

    except Exception as e:
        return f"Error: {str(e)}"