from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class User:
    user_id: str
    name: str
    email: str


@dataclass
class Ride:
    ride_id: str
    driver_id: str
    origin: str
    destination: str
    datetime_iso: str
    total_seats: int
    available_seats: int
    status: str = "active"  # active | canceled | finished
    passengers: List[str] = field(default_factory=list)
    notes: Optional[str] = None

    def datetime(self) -> datetime:
        return datetime.fromisoformat(self.datetime_iso)
