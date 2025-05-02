
# File Sharing Website

A simple file sharing website built with Python.

## 🚀 About

This project provides a basic platform for users to upload and share files.

## 🛠️ Built With

*   Python

## ⚙️ Installation

1.  **Prerequisites:**

    *   Python 3.6+
    *   pip (Python package installer)

2.  **Clone the repository:**

    ```bash
    git clone https://github.com/anshgupta517/file-sharing-website.git
    cd file-sharing-website
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt # If a requirements.txt file exists.  If not, install dependencies manually.
    ```

4.  **Database Setup:**

    This project uses `db.sqlite3`.  You may need to run migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

5.  **Run the server:**

    ```bash
    python manage.py runserver
    ```

    The website will be accessible at `http://localhost:8000/` (or the address shown in the terminal).

## ✨ Key Features

*   File Upload
*   File Sharing
