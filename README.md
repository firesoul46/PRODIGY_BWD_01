# 🧑‍💻 Flask CRUD API for Users

This is a simple RESTful API built with **Flask** that supports basic **CRUD operations** (Create, Read, Update, Delete) on a `users` resource. Data is stored in-memory using a Python dictionary, and each user has a UUID, name, email, and age.

---

## 🚀 Features

- Create a new user with a unique UUID
- Retrieve all users or a single user by ID
- Update user information
- Delete a user
- Input validation (email format, data types)
- Proper HTTP status codes and error messages

---

## 📦 Requirements

- Python 3.7+
- Flask

Install Flask using pip:

```bash
pip install flask
```

---

## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/firesoul46/PRODIGY_BWD_01
   cd PRODIGY_BWD_01
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

3. API will be available at:  
   ```
   http://localhost:5000
   ```

---

## 📬 API Endpoints

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| POST   | `/users`         | Create a new user        |
| GET    | `/users`         | Get all users            |
| GET    | `/users/<id>`    | Get a user by ID         |
| PUT    | `/users/<id>`    | Update a user by ID      |
| DELETE | `/users/<id>`    | Delete a user by ID      |

---

## 📝 Example JSON Body

### Create/Update User

```json
{
  "name": "Syed",
  "email": "syed@example.com",
  "age": 25
}
```

---

## ⚠️ Notes

- This app uses in-memory storage. Data will reset when the server restarts.
- Email format and data types are validated before processing requests.

---

