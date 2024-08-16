import openai
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


def generate_cv(questionnaire_data, api_key):
    openai.api_key = api_key
    prompt = (
        f"You are looking for a job and need to adjust your CV according to the following details.\n"
        f"Personal Information:\n"
        f"Name: {questionnaire_data['full_name']}\n"
        f"Age: {questionnaire_data['age']}\n"
        f"Address: {questionnaire_data['address']}\n"
        f"Contact Number: {questionnaire_data['contact_number']}\n"
        f"Email: {questionnaire_data['email']}\n"
        f"Nationality: {questionnaire_data['nationality']}\n"
        f"Work Permit: {questionnaire_data['work_permit']}\n"
        f"Education Level: {questionnaire_data['education_level']}\n"
        f"Field of Study: {questionnaire_data['field_of_study']}\n"
        f"Institutions: {questionnaire_data['institutions']}\n"
        f"Certifications: {questionnaire_data['certifications']}\n"
        f"Languages Spoken: {questionnaire_data['languages']}\n"
        f"Language Proficiency: {questionnaire_data['language_proficiency']}\n"
        f"Work Experience: {questionnaire_data['work_experience']}\n"
        f"Volunteer Experience: {questionnaire_data['volunteer_experience']}\n"
        f"Skills: {questionnaire_data['skills']}\n"
        f"Software Proficiency: {questionnaire_data['software_proficiency']}\n"
        f"Portfolio: {questionnaire_data['portfolio']}\n"
        f"Relocation: {questionnaire_data['relocation']}\n"
        f"References: {questionnaire_data['references']}\n\n"
        f"Generate a new text CV based on the above information: (do not add details that are not true)"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )
    generated_cv = response.choices[0].message['content'].strip()
    return generated_cv


class QuestionnaireView(LoginRequiredMixin, View):

    def get(self, request):
        # Render the questionnaire form
        return render(request, 'questionnaire.html')

    def post(self, request):
        # Process the submitted questionnaire data
        data = {
            'full_name': request.POST.get('full_name'),
            'age': request.POST.get('age'),
            'address': request.POST.get('address'),
            'contact_number': request.POST.get('contact_number'),
            'email': request.POST.get('email'),
            'nationality': request.POST.get('nationality'),
            'work_permit': request.POST.get('work_permit'),
            'education_level': request.POST.get('education_level'),
            'field_of_study': request.POST.get('field_of_study'),
            'institutions': request.POST.get('institutions'),
            'certifications': request.POST.get('certifications'),
            'languages': request.POST.get('languages'),
            'language_proficiency': request.POST.get('language_proficiency'),
            'work_experience': request.POST.get('work_experience'),
            'volunteer_experience': request.POST.get('volunteer_experience'),
            'skills': request.POST.get('skills'),
            'software_proficiency': request.POST.get('software_proficiency'),
            'portfolio': request.POST.get('portfolio'),
            'relocation': request.POST.get('relocation'),
            'references': request.POST.get('references'),
        }

        # Generate the CV using OpenAI
        api_key = 'sk-'
        generated_cv = generate_cv(data, api_key)

        # Save the generated CV to the session or process it as needed
        request.session['current_cv'] = generated_cv

        # Redirect to a page where the user can view or download the generated CV
        return redirect('upload_job_file')  # Replace with your actual view name for viewing the generated CV
