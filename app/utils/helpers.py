import logging
from datetime import datetime, timedelta
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


def log_request(request_type: str, endpoint: str, user_id: Optional[int] = None):
    """Log API requests"""
    logger.info(f"{request_type} {endpoint}" + (f" - User: {user_id}" if user_id else ""))


def calculate_expiry(minutes: int) -> datetime:
    """Calculate token expiry time"""
    return datetime.utcnow() + timedelta(minutes=minutes)
