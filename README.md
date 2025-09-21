# 🚀 FastAPI Stripe Payments API

A sample project built with **FastAPI**, **Pydantic**, and **Stripe API** to handle user authentication and payment processing.  

This project demonstrates:  
- JWT Authentication  
- User Registration & Login  
- Password hashing with `passlib`  
- Stripe Payment Integration (`PaymentIntents`)  
- Secure API endpoints  

---

## 🛠 Tech Stack
- Python 3.12  
- FastAPI  
- SQLAlchemy + SQLite (can be swapped with PostgreSQL/MySQL)  
- Pydantic  
- JWT (`pyjwt`)  
- Stripe API  

---

## 📂 Project Structure


fastapi_stripe_payments/
│── app/
│ ├── main.py # FastAPI entrypoint
│ ├── auth.py # JWT + password hashing
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── database.py # Database config
│ ├── payments.py # Stripe integration
│── requirements.txt



---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/fastapi-stripe-payments.git
cd fastapi-stripe-payments
```

### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.\.venv\Scripts\activate    # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Configure environment variables
Create a .env file in the project root:
```bash
SECRET_KEY=your_secret_key_here
STRIPE_SECRET_KEY=your_stripe_secret_key
```

### 5️⃣ Run the server
```bash
uvicorn app.main:app --reload
```


| File                 | Description                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **main.py**          | Entry point of FastAPI app. Defines routes for auth and includes Stripe payment router. Also handles JWT dependency for protected endpoints. |
| **auth.py**          | Handles JWT token creation, verification, password hashing, and password verification using `passlib`.                                       |
| **models.py**        | SQLAlchemy models for database tables. Includes `User` table (can add `Payment` table later).                                                |
| **schemas.py**       | Pydantic models for request validation and response serialization (e.g., UserCreate, UserLogin, PaymentRequest).                             |
| **database.py**      | Database configuration using SQLAlchemy (engine, session, Base). Handles DB connections.                                                     |
| **payments.py**      | Contains Stripe integration logic and payment-related endpoints. Defines `/create-payment-intent/` and other payment APIs.                   |
| **requirements.txt** | Lists all Python dependencies needed to run the project.                                                                                     |
| **.env**             | Environment variables (JWT secret, Stripe API key, database URL) to keep sensitive info out of code.                                         |
