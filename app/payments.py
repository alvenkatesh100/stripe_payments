import stripe
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, database
from .main import get_current_user

router = APIRouter()
stripe.api_key = "your_stripe_secret_key"

@router.post("/create-payment-intent/")
def create_payment(payment: schemas.PaymentRequest, db: Session = Depends(database.SessionLocal), user: dict = Depends(get_current_user)):
    try:
        intent = stripe.PaymentIntent.create(
            amount=payment.amount,
            currency=payment.currency,
            description=payment.description,
        )
        return {"client_secret": intent.client_secret}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
