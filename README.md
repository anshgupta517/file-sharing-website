
# File Sharing Website - Django

A simple file sharing website built with Django Python.

## 🚀 About

This project provides a basic platform for users to upload and share files.
* Implemented core features including user registration and authentication with password hashing, session-based login persistence, file uploading with metadata (title, description), and deletion capabilities.
* Designed views to display all files and user-specific files categorized by type (image, video, audio, PDF).
* Leveraged Django ORM for database modeling and interaction, the messages framework for user notifications, and the template engine for dynamic content rendering.

## 🛠️ Built With

*   Python

## ⚙️ Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/anshgupta517/file-sharing-website.git
    cd file-sharing-website
    ```


2.  **Database Setup:**

    This project uses `db.sqlite3`.  You may need to run migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

3.  **Run the server:**

    ```bash
    python manage.py runserver
    ```

    The website will be accessible at `http://localhost:8000/` (or the address shown in the terminal).

## ✨ Key Features

*   File Upload
*   File Sharing
