# PrintPoint Backend

This is the backend for the PrintPoint application, a platform for managing printing orders.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/printpoint-backend.git
    cd printpoint-backend
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the database:**

    - This project uses PostgreSQL. Make sure you have it installed and running.
    - Create a database and a user for the application.

5.  **Configure environment variables:**

    - Create a `.env` file in the root directory by copying the example file:
      ```bash
      cp .env.example .env
      ```
    - Update the `.env` file with your database credentials:
      ```
      DB_NAME=your_db_name
      DB_USER=your_db_user
      DB_PASSWORD=your_db_password
      DB_HOST=localhost
      DB_PORT=5432
      ```

6.  **Run the database migrations:**

    ```bash
    python manage.py migrate
    ```

7.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.
