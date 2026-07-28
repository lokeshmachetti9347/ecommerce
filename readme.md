# 🛒 E-Commerce CRUD Application using FastAPI

## 📌 Project Overview

This is a simple **E-Commerce CRUD Application** built using **FastAPI**, **SQLAlchemy**, and **MySQL**. The project demonstrates how to build RESTful APIs for managing products in an e-commerce system.

The application allows users to create, read, update, and delete product records while storing data in a MySQL database.

---

## 🚀 Features

* Add a new product
* View all products
* View a product by ID
* Update product details
* Delete a product
* Filter products by category (if implemented)
* Automatic API documentation using Swagger UI

---

## 🛠️ Technologies Used

* Python
* FastAPI
* SQLAlchemy
* MySQL
* PyMySQL
* Pydantic
* Uvicorn
* Requests Library (for API Testing)

---

## 📂 Project Structure

```text
Ecommerce_CRUD/
│
├── main.py          # FastAPI application and API routes
├── database.py      # Database connection
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic schemas
├── crud.py          # CRUD operations
├── requirements.txt # Project dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ecommerce-crud-fastapi.git
```

```bash
cd ecommerce-crud-fastapi
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pymysql
pip install pydantic
pip install requests
```

Or install everything using:

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Configuration

Create a MySQL database.

```sql
CREATE DATABASE ecommerce_db;
```

Update the database connection in `database.py`.

Example:

```python
DATABASE_URL = "mysql+pymysql://root:YourPassword@localhost:3306/ecommerce_db"
```

> If your password contains `@`, replace it with `%40`.

Example:

```python
DATABASE_URL = "mysql+pymysql://root:Lokesh%40123@localhost:3306/ecommerce_db"
```

---

## ▶️ Run the Project

```bash
uvicorn main:app --reload
```

Server URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

| Method | Endpoint                  | Description                                 |
| ------ | ------------------------- | ------------------------------------------- |
| GET    | /                         | Welcome API                                 |
| POST   | /products                 | Create Product                              |
| GET    | /products                 | Get All Products                            |
| GET    | /products/{id}            | Get Product by ID                           |
| PUT    | /products/{id}            | Update Product                              |
| DELETE | /products/{id}            | Delete Product                              |
| GET    | /category/{category_name} | Get Products by Category *(if implemented)* |

---

## 🧪 API Testing

The APIs were tested using:

* FastAPI Swagger UI
* Python Requests Library

Supported HTTP Methods:

* GET
* POST
* PUT
* DELETE

---

## 📚 Learning Outcomes

Through this project, I learned:

* Building REST APIs using FastAPI
* SQLAlchemy ORM
* MySQL database integration
* CRUD Operations
* Pydantic data validation
* API testing using Requests
* Swagger API documentation

---

## 📸 Project Demo

You can add:

* Project screenshots
* Swagger UI screenshots
* MySQL database screenshots
* Screen recording/demo video

---

## 👨‍💻 Author

**Lokesh Machetti**

* Python Developer (Learning)
* Backend Development Enthusiast
* Passionate about FastAPI, SQL, and Python
