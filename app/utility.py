import random
from typing import Dict
from pathlib import Path
from app.config import settings
from datetime import datetime


TEMPLATE_DIR = Path(__file__).parent / "templates"
TEMPLATE_DIR.mkdir(exist_ok=True)


def generate_otp_code() -> str:
    return str(random.randint(100000, 999999))


# Custom Jinja2 filters
def date_filter(value, format_str="%Y-%m-%d"):
    """Custom date filter for Jinja2 templates"""
    if isinstance(value, str) and value == "now":
        value = datetime.now()
    elif isinstance(value, str):
        try:
            value = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except:
            return value

    if isinstance(value, datetime):
        return value.strftime(format_str)
    return str(value)
