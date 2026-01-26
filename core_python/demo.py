# core_python/demo.py

"""
Demo script for UniCar core logic.

This file demonstrates the main business flows:
- user creation
- ride creation
- passenger joining and leaving a ride
- ride cancellation

It is intended for demonstration, testing, and portfolio purposes.
"""

from core_python.repository import JsonRepository
from core_python.services import UniCarService


def main():
    # Initialize repository (local JSON storage)
    repo = JsonRepository("data.json")
    service = UniCarService(repo)

    # -----------------------------
    # Create users
    # -----------------------------
    driver = service.create_user(
        name="Leonardo Oliveira",
        email="driver@unicar.app",
    )

    passenger = service.create_user(
        name="Maria Silva",
        email="passenger@unicar.app",
    )

    print("Driver created:", driver)
    print("Passenger created:", passenger)

    # -----------------------------
    # Create ride
    # -----------------------------
    ride = service.create_ride(
        driver_id=driver.user_id,
        origin="UNIFAL Campus",
        destination="Downtown",
        datetime_iso="2026-01-26T18:30:00",
        total_seats=3,
        notes="Evening ride",
    )

    print("\nRide created:")
    print(ride)

    # -----------------------------
    # Passenger joins ride
    # -----------------------------
    ride = service.join_ride(
        ride_id=ride.ride_id,
        user_id=passenger.user_id,
    )

    print("\nPassenger joined the ride:")
    print(ride)

    # -----------------------------
    # Passenger leaves ride
    # -----------------------------
    ride = service.leave_ride(
        ride_id=ride.ride_id,
        user_id=passenger.user_id,
    )

    print("\nPassenger left the ride:")
    print(ride)

    # -----------------------------
    # Driver cancels ride
    # -----------------------------
    ride = service.cancel_ride(
        ride_id=ride.ride_id,
        driver_id=driver.user_id,
    )

    print("\nRide canceled:")
    print(ride)


if __name__ == "__main__":
    main()
