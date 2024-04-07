import re
from datetime import datetime


def getDay(date: datetime = datetime.today()) -> datetime:

    return date.strftime("%Y-%m-%d")


def getToday() -> dict:
    return {"date_from": getDay(), "date_to": getDay()}


def verifyIP(ip_address: str) -> bool:

    pattern = r"^10\.8\.126\.[0-9]{1,3}$"
    match = re.match(pattern, ip_address)
    if match:
        return True
    return False
