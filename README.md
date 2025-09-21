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
