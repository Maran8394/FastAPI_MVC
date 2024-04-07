## Installation Guide

Follow these steps to set up and run the application:

### Step 1: Install Dependencies
First, install the required dependencies by executing the following command in your terminal:

```bash
pip install -r requirements.txt
```

### Step 2: Configure Database Connection
Navigate to the `database/__init__.py` file and update the `DB_URL` variable with your MySQL database connection details:

```python
DB_URL = "mysql+mysqldb://username:password@localhost/db_name"
```

Replace `username`, `password`, and `db_name` with your MySQL credentials and database name.

### Step 3: Verify Folder Contents
Ensure that the folder you have opened contains the `main.py` file.

### Step 4: Run the Application
To start the application, execute the following command:

```bash
uvicorn main:app --reload
```

This command will launch the application with automatic reloading enabled for development purposes.

By following these steps, you should have the application up and running successfully.
