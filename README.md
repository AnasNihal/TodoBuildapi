# 📝 TodoBuildAPI

A full-stack **Todo List Web Application** powered by **Django REST Framework** (DRF) for backend APIs and **vanilla JavaScript** for the frontend. This project demonstrates real-time fetching, editing, and deleting of todos via RESTful APIs — no page reloads, no heavy frontend frameworks.

---

## 🚀 Features

- ✅ Fetch todo list via DRF-based API
- ✍️ Edit todos inline with live save
- 🗑️ Delete todos dynamically via JavaScript
- 📬 JSON-based communication using DRF serializers
- ⚙️ `@csrf_exempt` for non-form JavaScript requests
- ⚡ Clean, minimal UI using native JS and HTML

---

## 🛠️ Tech Stack

| Layer       | Technology           |
|-------------|----------------------|
| Backend     | Django + Django REST Framework |
| API Format  | JSON (DRF Serializers + Views) |
| Frontend    | HTML, Tailwind CSS, Vanilla JavaScript |
| DB          | SQLite (default)     |

---

## 📂 Project Structure

TodoBuildapi/
├── todos/
│ ├── migrations/
│ ├── templates/
│ ├── static/
│ ├── models.py
│ ├── views.py ← API logic with DRF
│ ├── serializers.py ← DRF serializers
│ └── urls.py
├── TodoBuildapi/
│ └── settings.py
└── manage.py


📦 Setup Instructions

1. Clone the Repository**
   ```bash
   git clone https://github.com/AnasNihal/TodoBuildapi.git
   cd TodoBuildapi
Create and activate virtual environment

python -m venv venv
# source venv/bin/activate  
# Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Apply migrations
python manage.py makamigrations
python manage.py migrate

Start the development server
python manage.py runserver

Open your browser
http://127.0.0.1:8000/
