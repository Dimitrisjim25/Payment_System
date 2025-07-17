import os
from pathlib import Path
from typing import Any

import stripe
from dotenv import load_dotenv

# Ρητή φόρτωση του .env από το root του project
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def create_checkout_session(amount: int, success_url: str, cancel_url: str) -> Any:
    try:
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": "Go for EAT Payment"},
                        "unit_amount": int(amount * 100),  # Σε cents
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=success_url,
            cancel_url=cancel_url,
            customer_email="example@domain.com",
        )
        return session
    except Exception as e:
        raise Exception(f"Stripe error: {str(e)}")
