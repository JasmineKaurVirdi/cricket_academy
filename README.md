# My Web Project
A dynamic web application using Django to manage a Cricket Academy. This project features a comprehensive Admin Dashboard for complete control over academy data. Key features include: CRUD (Create, Read, Update, Delete) functionality for managing Coaches and Programs, a dedicated section for Fee Management, and public-facing pages for Admission Forms, Program Listings, and a Gallery. It serves as the single source of truth for all academy-related information.


# Features
The application is designed to be a comprehensive management solution for a Cricket Academy.

### Core Functionality
 * User Authentication & Access Control:
   * Secure Login (login.html) and Registration (register.html) system for students, parents, and administrators.
   * Dedicated Admin Login (admin_login.html) for management access.
 * Intuitive Dashboards:
   * A main Dashboard (dashboard.html) for general users.
   * A robust Admin Dashboard for complete system oversight.

### Management Modules (Admin Access)
The administrative section provides CRUD (Create, Read, Update, Delete) operations for core academy data:
 * Coach Management: Manage and update coach profiles, details, and certifications. (admin/manage_coaches.html, admin/edit_coach.html)
 * Program Management: Create, modify, and list all training programs offered by the academy. (admin/manage_programs.html)
 * Fee Management: Control fee structures, track payments, and update fee records. (admin/manage_fees.html, admin/edit_fee.html)
 * Gallery Management: Upload and manage images/videos for the academy's public gallery. (admin/manage_gallery.html)

### Student & Public Modules
 * Online Admissions: Streamlined form for new student applications. (core/admission_form.html)
 * Program Display: Publicly list all available training programs with details. (programs.html)
 * Academy Gallery: Showcase academy photos, facilities, and events to the public. (gallery.html)
 * Contact Information: Dedicated page for academy contact details and inquiries. (contact.html - Inferred from folder structure)
 * Coach Directory: View profiles and details of the academy's coaching staff. (coaches.html)


# Tech Stack
This project is built as a *Full-Stack Web Application* using the following core technologies:

### Backend & Core Framework
* *Django (Python):* The high-level web framework used for robust, rapid development and the core logic.
* *Python:* The primary programming language.

### Database
* *SQLite:* Used as the default database for development (db.sqlite3).

### Frontend & UI
* *HTML (Django Templating):* For structuring the web pages.
* *CSS / JavaScript:* For styling and client-side interactivity.
* *Bootstrap:* For ensuring a responsive and modern user interface.

### Installation
Follow these steps to set up the CricketAcademy project locally:

1. *Clone the repository:*
```bash
git clone https://github.com/JasmineKaurVirdi/cricket_academy.git

2. Navigate to the project folder:

cd cricket_academy

3. Create a virtual environment (recommended)

python -m venv venv

4. Activate the virtual environment:
Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

5. Install dependencies:

pip install -r requirements.txt

6. Apply migrations to set up the database:

python manage.py migrate

7. Create a superuser for admin access (optional but recommended):

python manage.py createsuperuser

8. Run the development server:

python manage.py runserver

9. Access the project in your browser:

Admin panel: http://127.0.0.1:8000/admin/

Core/student area: http://127.0.0.1:8000/

📌 Contributing

Fork the repository

Create a new branch

Make changes and commit

Open a Pull Request


📧 Created By

Author: Jasmine Kaur

