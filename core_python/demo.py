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

from core_python.models import User
from core_python.repository import JsonRepository
from core_python.services import OfferInput, UniCarService


def main():
    # Initialize repository (local JSON storage)
    repo = JsonRepository("data.json")
    service = UniCarService(repo)

    # -----------------------------
    # Create users
    # -----------------------------
    driver = service.upsert_user(
        User(
            user_id="driver-001",
            name="Sample Driver",
            email="driver@example.com",
            phone="+55 00 00000-0000",
            car_model="Example vehicle",
            car_color="Blue",
            plate="ABC1D23",
            stops=["Central Square", "Bus Station"],
        )
    )

    passenger = service.upsert_user(
        User(
            user_id="passenger-001",
            name="Sample Passenger",
            email="passenger@example.com",
            phone="+55 00 00000-0000",
        )
    )

    print("Driver created:", driver)
    print("Passenger created:", passenger)

    # -----------------------------
    # Create an offer
    # -----------------------------
    offer = service.create_offer(OfferInput(
        driver_id=driver.user_id,
        seats=3,
        departure_label="UNIFAL Campus",
        destination_label="Downtown",
        hour="18",
        minute="30",
        stops_text="Central Square|Bus Station",
        car_model=driver.car_model,
        car_color=driver.car_color,
        plate=driver.plate,
    ))

    print("\nOffer created:")
    print(offer)

    # -----------------------------
    # Passenger selects and confirms the offer
    # -----------------------------
    service.select_offer(offer.offer_key)
    confirmed_offer = service.confirm_selected_offer()

    print("\nOffer after passenger confirmation:")
    print(confirmed_offer)

    # -----------------------------
    # Build the external communication message
    # -----------------------------
    message = service.build_whatsapp_message(
        passenger_name=passenger.name,
        pickup_point="Central Square",
    )

    print("\nGenerated passenger message:")
    print(message)


if __name__ == "__main__":
    main()
