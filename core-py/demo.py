# core_python/demo.py
from core_python.models import User
from core_python.services import UniCarService, OfferInput
from core_python.repository import JsonRepository


def main():
    repo = JsonRepository()
    service = UniCarService(repo)

    # -----------------------------
    # Create driver user
    # -----------------------------
    driver = User(
        user_id="driver_001",
        name="Leonardo Oliveira",
        email="driver@example.com",
        phone="(35) 99999-0000",
        car_model="Onix",
        car_color="Black",
        plate="ABC-1234",
        stops=["Campus", "Downtown"],
    )
    service.upsert_user(driver)

    # -----------------------------
    # Create carpool offer
    # -----------------------------
    offer_input = OfferInput(
        driver_id=driver.user_id,
        seats=2,
        departure_label="UNIFAL Campus",
        destination_label="Downtown",
        hour="18",
        minute="30",
        stops_text="Campus|Bus Station",
        car_model=driver.car_model,
        car_color=driver.car_color,
        plate=driver.plate,
    )

    offer = service.create_offer(offer_input)
    print("Offer created:", offer.offer_key)

    # -----------------------------
    # List available offers
    # -----------------------------
    offers = service.list_available_offers()
    for line in service.offers_to_list_strings(offers):
        print(line)

    # -----------------------------
    # Select offer (TinyDB simulation)
    # -----------------------------
    service.select_offer(offer.offer_key)

    # -----------------------------
    # Confirm carpool (seat -1)
    # -----------------------------
    updated_offer = service.confirm_selected_offer()
    print("Remaining seats:", updated_offer.available_seats)

    # -----------------------------
    # Build WhatsApp message
    # -----------------------------
    message = service.build_whatsapp_message(
        passenger_name="Passenger Example",
        pickup_point="Bus Station",
    )
    print("\nWhatsApp message:\n")
    print(message)


if __name__ == "__main__":
    main()
