# utils.py

import openai
openai.api_key = "sk-3"
# -3"
def generate_cv(current_cv, role_description, api_key):
    print("I am in generate cv")
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"You are looking for a job and needs to adjust you cv according to job description.\n Given the following CV:\n{current_cv}\n\nDescription of desired role:\n{role_description}\n\nGenerate a new text CV: (do not add details that are not true)",
        temperature=0.7,
        max_tokens=150
    )
    generated_cv = response.choices[0].text.strip()
    print(generated_cv)
    return generated_cv

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content



