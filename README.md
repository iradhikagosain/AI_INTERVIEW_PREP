# AI Interview Prep

This is a Django-based web application that helps users prepare for interviews using AI.  
Users can register, log in, upload their resumes, and receive AI-generated interview questions tailored to their skills and experience.

---

## 🚀 Features

- ✅ User Registration & Login  
- ✅ Secure Admin Panel (`customadmin` app)  
- ✅ Resume Upload with Text Extraction  
- ✅ Integration with llama3 to generate interview questions  
- ✅ Custom 404 pages and static file management using WhiteNoise  
- ✅ Production-ready deployment with Gunicorn and Render

---

## ⚙️ Tech Stack

- **Backend:** Django  
- **Frontend:** HTML, CSS, JavaScript (AdminLTE)  
- **AI Integration:** llama3 
- **Deployment:** Render.com  
- **WSGI Server:** Gunicorn  
- **Static Files:** WhiteNoise  

---

## 📁 Project Structure

ai_interview_project/
├── manage.py
├── myproject/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── users/ # Handles user registration & login
├── customadmin/ # Custom admin panel
├── templates/
├── static/
├── requirements.txt
├── Procfile
