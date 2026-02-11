import random
import hashlib
from datetime import datetime, timedelta


OTP_EXPIRY_MINUTES = 5


def generate_otp() -> str:
    """
    Generate a 6-digit numeric OTP
    """
    return str(random.randint(100000, 999999))


def hash_otp(otp: str) -> str:
    """
    Hash OTP using SHA256
    """
    return hashlib.sha256(otp.encode()).hexdigest()


def get_expiry_time():
    """
    Return expiry datetime (now + 5 minutes)
    """
    return datetime.utcnow() + timedelta(minutes=OTP_EXPIRY_MINUTES)