---

### **Student Management System**  

This system provides an efficient way for administrators to add, edit, and delete student details, track enrollments, and manage course information. Whether you're handling a small class or a large institution, this system helps reduce manual work, prevent errors, and keep student records easily accessible.

---

## **Features**  

-  **Add, Edit, Delete, and View Student Records**  
-  **Tailwind CSS UI (responsive, and clean design)**   
-  **Database Management with MariaDB (via XAMPP)**  

---

### **Prerequisites**  
Before setting up the project, ensure you have the following installed:  
- **Python** (version 3.10 or later)  
- **pip & pipenv** (for managing dependencies)  
- **MariaDB (via XAMPP)** (for database management)  
- **Git** (to clone the repository)  

Check if they're installed:  
```bash
python --version
pip --version
pipenv --version
git --version
```

If **pipenv** is not installed, install it using:  
```bash
pip install pipenv
```

---

### **Clone the Repository**  
```bash
git clone https://github.com/crudproject/stud_mgmt_sys.git
cd stud_mgmt_sys
```

### **Set Up Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate (For macOS/Linux)
venv\Scripts\activate (For Windows)
```

### **Configure Database (MariaDB XAMPP)**
- Start XAMPP & enable **Apache** and **MySQL**  
- Create a database in **phpMyAdmin**  
- Update `settings.py` with database credentials  

### **Apply Migrations**  
```bash
python manage.py makemigrations
python manage.py migrate
```

### **Run the Server**  
```bash
python manage.py runserver
```
Open **http://127.0.0.1:8000/** in browser.  

---

## **Project Structure**
```bash
stud_mgmt_sys/        # Root project directory  
│── stud_mgmt_sys/    # Django project folder (contains settings.py)  
│   │── __init__.py  
│   │── settings.py   # Main Django settings file  
│   │── urls.py       # Project-level URL configurations  
│   │── wsgi.py       # WSGI entry point for deployment  
│   │── asgi.py       # ASGI entry point for async servers  
│
│── stud_system/      # Main application directory  
│   │── migrations/   # Database migrations  
│   │── static/       # Static files (CSS, JS)  
│   │── templates/    # HTML templates  
│   │── __init__.py  
│   │── admin.py      # Django admin settings  
│   │── apps.py       # App configuration  
│   │── models.py     # Database models  
│   │── views.py      # Application logic  
│   │── urls.py       # App-level URL configurations  
│
│── manage.py         # Django management script  
```

