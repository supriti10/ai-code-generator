def code_prompt(user_input):
    return f"""
You are a strict coding assistant.

Follow these rules EXACTLY:
1. First give a title in this format:
   **<Topic Name>**
2. Then give only code inside a code block.
3. DO NOT include any comments in the code.
4. DO NOT include explanation.
5. DO NOT include time or space complexity.

{user_input}
"""

def explain_prompt(code):
    return f"""
Explain the following code step by step in simple terms:

{code}
"""

def debug_prompt(code):
    return f"""
Fix the errors in the following code and provide corrected version:

{code}
"""