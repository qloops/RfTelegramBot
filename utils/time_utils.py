from tzlocal import get_localzone
from datetime import (
    datetime, 
    timezone,
)

def convert_to_utc(dt: datetime) -> datetime:
    """
    Converts any datetime to UTC, assuming local time if naive.

    Args:
        dt: A datetime object (naive or timezone-aware).

    Returns:
        datetime: A timezone-aware datetime object in UTC.
    """
    if dt.tzinfo is None:
        local_tz = get_localzone()
        dt = dt.replace(tzinfo=local_tz)
    
    return dt.astimezone(timezone.utc)
