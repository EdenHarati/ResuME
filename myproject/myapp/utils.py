# utils.py

import openai
def generate_cv(current_cv, role_description, api_key):
    # openai.api_key = api_key
    # current_cv = "Name: Eden \n Age: 28 \n Role: Java Developer\n Year of experience: 1 year"
    # role_description = "we Are looking for a new developer with 2 years of Java experience, a good group work abilities"
    response = openai.Completion.create(
        # engine="text-davinci-003",
        # engine="gpt-3.5-turbo",
        # prompt=f"Given the following CV:\n{current_cv}\n\nDescription of desired role:\n{role_description}\n\nGenerate a new CV:",
        # temperature=0.7,
        # max_tokens=150
    )
    generated_cv = response.choices[0].text.strip()
    return generated_cv

generate_cv("Name: Eden \n Age: 28 \n Role: Java Developer\n Year of experience: 1 year", "we Are looking for a new developer with 2 years of Java experience, a good group work abilities", 3)