import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from stripe_utils import create_checkout_session

# Ρητή φόρτωση του .env από το root του project
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

app = FastAPI()


@app.get("/checkout/")
async def create_checkout_session_endpoint(price: int = 10) -> RedirectResponse:
    try:
        base_url = os.getenv("BASE_URL")
        checkout_session: Any = create_checkout_session(
            amount=price,
            success_url=f"{base_url}/success/",
            cancel_url=f"{base_url}/cancel/",
        )
        return RedirectResponse(checkout_session.url, status_code=303)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/success/")
async def payment_success() -> dict[str, str]:
    return {"message": "Payment successful"}


@app.get("/cancel/")
async def payment_cancel() -> dict[str, str]:
    return {"message": "Payment cancelled"}
