# Online File Manager


https://github.com/user-attachments/assets/5b26876e-ebae-4634-a09f-7a7501a94166


An online file management system built with Django, HTML, CSS, JavaScript, and SQL.

## Features

- **File Upload**: Upload files to the server.
- **File Management**: Organize files, rename, and delete.
- **User Authentication**: Secure login and registration to manage personal files.
- **Responsive Design**: Accessible from both desktop and mobile devices.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQL (e.g., SQLite, PostgreSQL, MySQL)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YourUsername/OnlineFileManager.git
   cd OnlineFileManager
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database**

   - Update the `DATABASES` section in `settings.py` with your SQL database configuration.

5. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   Open `http://127.0.0.1:8000/` in your web browser to access the file manager.

## Usage

1. **Register**: Create an account to manage your files.
2. **Login**: Log in with your credentials.
3. **Upload Files**: Use the interface to upload and organize your files.
4. **Manage Files**: Rename, move, and delete files as needed.

## Contributing

1. **Fork the Repository**: Click the "Fork" button on GitHub.
2. **Create a Branch**: `git checkout -b feature/YourFeature`
3. **Commit Changes**: `git commit -am 'Add new feature'`
4. **Push to Branch**: `git push origin feature/YourFeature`
5. **Create a Pull Request**: Open a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Django Documentation**: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- **SQL Documentation**: [PostgreSQL](https://www.postgresql.org/docs/), [MySQL](https://dev.mysql.com/doc/)
