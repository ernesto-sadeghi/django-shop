# 📝 Django Blog Website  

A simple blog application built with **Django** for learning purposes.  
The project includes user authentication, article posting with tags, a comment system, search functionality, and pagination.  

---

## 🚀 Features  

- 🔐 **User Authentication**  
  - Sign up, log in, and log out.  

- 📰 **Blog Articles**  
  - Create, read, update, and delete articles.  
  - Each article can have multiple tags.  

- 💬 **Comments System**  
  - Users can comment on articles.  
  - Comments are linked to the article and user.  

- 🔍 **Search**  
  - Search articles by title or content.  

- 📑 **Pagination**  
  - Paginated article list for better navigation.  

---

## 🛠️ Tech Stack  

- **Backend**: Django, Django ORM  
- **Database**: SQLite (default, easy to switch to PostgreSQL/MySQL)  
- **Frontend**: Django Templates ( custom CSS)    

---
## Project structure
django-shop/
│-- blog/                # Main blog app (articles, tags, comments)
│-- accounts/            # Authentication (signup, login, logout)
│-- templates/           # HTML templates
│-- static/              # CSS, JS, images
│-- manage.py
│-- requirements.txt



---

## ⚙️ Installation  

Clone the repository:  
```bash
git clone https://github.com/your-username/django-blog.git
cd django-blog
