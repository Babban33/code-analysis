import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

genai.configure(api_key=os.getenv("KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
code = """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
"""
prompt = f"""
    Analyze the following code snippet for:
    - Code quality
    - Performance
    - Readability
    - Security vulnerabilities
    - Suggestions for improvement
    
    Code snippet:
    ```python
    {code}
    ```

    Provide a detailed analysis and rate the code on a scale of 1 to 10 for each category.
    """
response = model.generate_content(prompt)
print(response.text)