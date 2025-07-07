# 🧠 Smart Todo AI – Backend

This is the **backend** API service for the Smart Todo AI application, a smart task manager that leverages AI to help users organize and prioritize tasks using context-aware suggestions.

---

## 🚀 Tech Stack

- **Framework:** Django 4+ with Django REST Framework
- **Database:** PostgreSQL via [Supabase](https://supabase.com/)
- **AI Integration:** OpenRouter (supports OpenAI, Claude, Gemini, etc.)
- **Authentication:** Basic Django Auth (JWT or OAuth2 optional)
- **Hosting-ready:** Designed for deployment with Render, Railway, or Supabase edge functions

---

## 📁 Folder Structure

backend/
├── tasks/ # App for managing tasks
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
├── context/ # App for handling context data
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
│
├── ai/ # Optional: App for AI integrations
│ ├── views.py
│ └── utils.py
│
├── smarttodo/ # Django project settings
│ ├── settings.py
│ └── urls.py
│
├── manage.py
└── requirements.txt

---

## 🧩 Features

- ✅ RESTful API endpoints for managing tasks, categories, and context data
- 🧠 AI endpoint for:
  - Task prioritization based on context
  - Deadline suggestions
  - Smart category and tag recommendations
- 📂 Supabase-hosted PostgreSQL database
- 🔐 Clean, modular, scalable backend with extensible AI interface

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-todo-backend.git
cd smart-todo-backend
```

### 3. Install Requirements

```bash

pip install -r requirements.txt
```

### 4. Connect to Supabase (PostgreSQL)

Update your settings.py database configuration:

# smarttodo/settings.py

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'postgres',
'USER': 'postgres.wupdktasksrfhiwzqnva',
'PASSWORD': 'your-password',
'HOST': 'aws-0-ap-south-1.pooler.supabase.com',
'PORT': '5432',
}
}

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Development Server

python manage.py runserver
Server will run at http://localhost:8000/

## 🔌 API Endpoints

| Method | Endpoint           | Description                            |
| ------ | ------------------ | -------------------------------------- |
| GET    | `/api/tasks/`      | Retrieve all tasks                     |
| POST   | `/api/tasks/`      | Create a new task (AI-enhanced)        |
| GET    | `/api/categories/` | Get all categories/tags                |
| POST   | `/api/context/`    | Add daily context (email, notes, etc.) |
| GET    | `/api/context/`    | Retrieve context history               |
| POST   | `/api/ai/suggest/` | 🔥 Get AI-powered task suggestions     |

---

## 🧠 AI Integration

This project integrates with **[OpenRouter](https://openrouter.ai)**, allowing access to various cutting-edge models:

- **OpenAI** (GPT-4, GPT-3.5)
- **Claude** (Anthropic)
- **Gemini** (Google)
- **Mistral**, **LLaMA**, and more via **LM Studio** (optional for local inference)

### 📡 AI Pipeline

The AI backend:

- Accepts task title, description, and context data
- Uses LLMs to analyze and suggest:
  - Priority score
  - Enhanced description
  - Realistic deadline
  - Relevant category/tags

---

## ✅ Benefits of AI in SmartTodo

- **Context-Aware Suggestions**  
  Understands the intent of the task using natural language context from notes, messages, or email.

- **Auto Prioritization**  
  Assigns priority scores based on urgency, category, workload, and schedule.

- **Deadline Estimation**  
  Suggests practical deadlines, improving task planning and focus.

- **Category/Tag Auto-Suggestion**  
  Recommends the most appropriate categories/tags, reducing user friction.

- **Enhanced Task Descriptions**  
  Converts vague task inputs into clear, actionable descriptions using AI refinement.

---

### 📌 Environment Variables

Create a .env file for secret keys:

```bash
OPENROUTER_API_KEY=your_openrouter_key
DJANGO_SECRET_KEY=your_secret
DEBUG=True
Use python-decouple or os.environ.get() to load securely.
```
# smarttodo-backend
