from dotenv import load_dotenv
import os
from pathlib import Path

# Φορτώνει .env από τον φάκελο που περιέχει αυτό το αρχείο
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# Εκτυπώνει για έλεγχο
print("STRIPE_SECRET_KEY:", os.getenv("STRIPE_SECRET_KEY"))
print("STRIPE_PUBLISHABLE_KEY:", os.getenv("STRIPE_PUBLISHABLE_KEY"))
print("BASE_URL:", os.getenv("BASE_URL"))



