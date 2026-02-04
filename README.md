# User Management System – Django

A role-based user management system built using **Django** and **PostgreSQL**, supporting **Admin** and **User** roles with secure authentication and authorization.

---

## Features
- Role-based login (Admin / User)
- Secure authentication
- Admin dashboard to manage users (Add, View, Delete)
- User dashboard with restricted access
- Audit fields (`createdOn`, `lastUpdatedOn`)
- PostgreSQL integration using Django ORM

---

## Tech Stack
- **Backend:** Python, Django  
- **Database:** PostgreSQL  
- **ORM:** Django ORM  
- **Frontend:** HTML, CSS  

---

## Setup
```bash
git clone https://github.com/your-username/user-management-system.git
cd user-management-system
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
