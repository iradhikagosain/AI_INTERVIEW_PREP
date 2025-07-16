from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import CustomUserCreationForm, ProfileUpdateForm,ResumeForm
from .models import Resume
from .extract import extract_text_from_pdf  # extraction function
from .ai_local import get_interview_questions # Gemini API function




# Register view
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('upload_resume')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Logout view (POST only)
@require_POST
def logout_view(request):
    logout(request)
    return redirect('home')

# Safe profile edit view using form
@login_required
def edit_profile(request):
    user = request.user

    if user.is_superuser:
        return redirect('home')

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, 'users/edit_profile.html', {'form': form})

# Delete account view
@login_required
def delete_account(request):
    user = request.user

    if user.is_superuser:

        return redirect('home')

    if request.method == 'POST':
        user.delete()
        return redirect('home')

    return render(request, 'users/delete_account.html')



import re

@login_required
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user  
            resume.save()

            file_path = resume.file.path  

           
            extracted_text = extract_text_from_pdf(file_path)

           
            raw_output = get_interview_questions(extracted_text)
            print('RAW LLM OUTPUT:\n', raw_output)


            
            pattern = r"(Q\d+:.*?A\d+:.*?)(?=Q\d+:|$)"
            blocks = re.findall(pattern, raw_output, re.DOTALL)

            qas = []
            for block in blocks:
                match = re.search(r"(Q\d+:\s.*?)(A\d+:\s.*)", block, re.DOTALL)
                if match:
                    question = match.group(1).strip()
                    answer = match.group(2).strip()
                    qas.append({'question': question, 'answer': answer})

            
            formatted = '\n\n'.join([f"{qa['question']}\n{qa['answer']}" for qa in qas])
            resume.generated_questions = formatted
            resume.save()

            return render(request, 'users/upload.html', {
                'form': form,
                'qas': qas   
            })
    else:
        form = ResumeForm()

    return render(request, 'users/upload.html', {'form': form})
