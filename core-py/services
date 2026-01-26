from typing import Dict, Any
from uuid import uuid4

from core_python.models import Ride, User
from core_python.repository import JsonRepository


class UniCarService:
    def __init__(self, repo: JsonRepository):
        self.repo = repo

    # ---------- Users ----------
    def create_user(self, name: str, email: str) -> User:
        data = self.repo.get_all()
        user_id = str(uuid4())
        user = User(user_id=user_id, name=name, email=email)
        data["users"][user_id] = {"user_id": user.user_id, "name": user.name, "email": user.email}
        self.repo.save_all(data)
        return user

    # ---------- Rides ----------
    def create_ride(
        self,
        driver_id: str,
        origin: str,
        destination: str,
        datetime_iso: str,
        total_seats: int,
        notes: str | None = None,
    ) -> Ride:
        if total_seats <= 0:
            raise ValueError("total_seats must be >= 1")

        data = self.repo.get_all()
        if driver_id not in data["users"]:
            raise ValueError("driver_id not found")

        ride_id = str(uuid4())
        ride = Ride(
            ride_id=ride_id,
            driver_id=driver_id,
            origin=origin,
            destination=destination,
            datetime_iso=datetime_iso,
            total_seats=total_seats,
            available_seats=total_seats,
            notes=notes,
        )
        data["rides"][ride_id] = self._ride_to_dict(ride)
        self.repo.save_all(data)
        return ride

    def join_ride(self, ride_id: str, user_id: str) -> Ride:
        data = self.repo.get_all()
        ride = self._load_ride(data, ride_id)

        if user_id not in data["users"]:
            raise ValueError("user_id not found")

        if ride.status != "active":
            raise ValueError("ride is not active")

        if user_id == ride.driver_id:
            raise ValueError("driver cannot join as passenger")

        if user_id in ride.passengers:
            return ride  # idempotente: já está dentro

        if ride.available_seats <= 0:
            raise ValueError("no available seats")

        ride.passengers.append(user_id)
        ride.available_seats -= 1

        data["rides"][ride_id] = self._ride_to_dict(ride)
        self.repo.save_all(data)
        return ride

    def leave_ride(self, ride_id: str, user_id: str) -> Ride:
        data = self.repo.get_all()
        ride = self._load_ride(data, ride_id)

        if user_id in ride.passengers:
            ride.passengers.remove(user_id)
            ride.available_seats += 1

        data["rides"][ride_id] = self._ride_to_dict(ride)
        self.repo.save_all(data)
        return ride

    def cancel_ride(self, ride_id: str, driver_id: str) -> Ride:
        data = self.repo.get_all()
        ride = self._load_ride(data, ride_id)

        if ride.driver_id != driver_id:
            raise ValueError("only the driver can cancel the ride")

        ride.status = "canceled"
        data["rides"][ride_id] = self._ride_to_dict(ride)
        self.repo.save_all(data)
        return ride

    # ---------- Helpers ----------
    def _load_ride(self, data: Dict[str, Any], ride_id: str) -> Ride:
        if ride_id not in data["rides"]:
            raise ValueError("ride_id not found")
        return self._dict_to_ride(data["rides"][ride_id])

    def _ride_to_dict(self, ride: Ride) -> Dict[str, Any]:
        return {
            "ride_id": ride.ride_id,
            "driver_id": ride.driver_id,
            "origin": ride.origin,
            "destination": ride.destination,
            "datetime_iso": ride.datetime_iso,
            "total_seats": ride.total_seats,
            "available_seats": ride.available_seats,
            "status": ride.status,
            "passengers": ride.passengers,
            "notes": ride.notes,
        }

    def _dict_to_ride(self, d: Dict[str, Any]) -> Ride:
        return Ride(
            ride_id=d["ride_id"],
            driver_id=d["driver_id"],
            origin=d["origin"],
            destination=d["destination"],
            datetime_iso=d["datetime_iso"],
            total_seats=d["total_seats"],
            available_seats=d["available_seats"],
            status=d.get("status", "active"),
            passengers=list(d.get("passengers", [])),
            notes=d.get("notes"),
        )
