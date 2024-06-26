<h1 style="text-align: center;">
  FisioAgendaApp-Pw2
</h1>

The purpose of this project is to develop an application for registering physiotherapy professionals to schedule appointments. The app aims to create a digital platform that makes it easier for patients to access physiotherapy services, while also offering professionals an effective tool to manage their appointments and improve the efficiency of their services. The application's main objective is to improve the accessibility and convenience of physiotherapy services, making scheduling appointments simpler and more efficient.


## Prerequisites

Make sure you have the following tools installed on your machine:

- An IDE (such as VSCode, PyCharm, etc.) or text editor of your choice
- Support for HTML, CSS, and JavaScript
- Python 3.10.8
- Django 5.0.4
- SQLite3

## How to Run

1. **Clone this repository to your local environment:**

    ```bash
    $ git clone https://github.com/ggomes12/FisioAgendaApp-Pw2.git
    ```

2. **Navigate to the project directory:**

    ```bash
    $ cd FisioAgendaApp-Pw2
    ```

3. **Create a virtual environment:**

    ```bash
    $ python3 -m venv env
    ```

4. **Activate the virtual environment:**

    - On Windows:
      ```bash
      $ env\Scripts\activate
      ```

    - On MacOS/Linux:
      ```bash
      $ source env/bin/activate
      ```

5. **Install the required dependencies:**

    ```bash
    $ pip install -r requirements.txt
    ```

6. **Apply the migrations to set up the database:**

    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

7. **Create a superuser (optional, for admin access):**

    ```bash
    $ python manage.py createsuperuser
    ```

8. **Run the application:**

    ```bash
    $ python manage.py runserver
    ```

9. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000`.

## Project Structure


## Key Files and Directories

- **clients/models.py**: Defines the database models for the application.
- **clients/forms.py**: Contains the form logic for user and client registration.
- **clients/views.py**: Handles the views logic for rendering pages and processing form submissions.
- **clients/templates/clients/**: Contains the HTML templates for the application.
- **clients/static/clients/**: Contains static files such as CSS, JavaScript, Images and Fonts .
- **fisioAgenda/settings.py**: Configuration for the Django project.
- **fisioAgenda/urls.py**: URL routing for the project.

## Functionality

### Registration

- Users can register as clients by filling out a form with their username, email, password, phone number, and address.
- Upon successful registration, the user is automatically logged in and redirected to their profile.

### Login

- Registered users can log in using their username and password.

### Profile

- After logging in, users can view and update their profile information.

## Troubleshooting

If you encounter any issues, try the following steps:

1. Ensure all dependencies are installed by running:
    ```bash
    $ pip install -r requirements.txt
    ```

2. Apply the latest migrations:
    ```bash
    $ python manage.py migrate
    ```

3. Check the server logs for any error messages.

4. If the issue persists, feel free to open an issue on the GitHub repository.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides an overview of the FisioAgenda application, instructions for setting up the development environment, and details about the project structure and functionality.



