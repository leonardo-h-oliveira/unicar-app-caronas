from core_python.repository import JsonRepository
from core_python.services import UniCarService


def main():
    repo = JsonRepository()
    svc = UniCarService(repo)

    driver = svc.create_user("Motorista Exemplo", "driver@exemplo.com")
    p1 = svc.create_user("Passageiro 1", "p1@exemplo.com")
    p2 = svc.create_user("Passageiro 2", "p2@exemplo.com")

    ride = svc.create_ride(
        driver_id=driver.user_id,
        origin="UNIFAL - Campus Poços",
        destination="Centro",
        datetime_iso="2026-02-01T18:30:00",
        total_seats=2,
        notes="Saída do estacionamento",
    )

    print("Ride created:", ride)

    ride = svc.join_ride(ride.ride_id, p1.user_id)
    print("After p1 joins:", ride.available_seats, ride.passengers)

    ride = svc.join_ride(ride.ride_id, p2.user_id)
    print("After p2 joins:", ride.available_seats, ride.passengers)

    ride = svc.leave_ride(ride.ride_id, p1.user_id)
    print("After p1 leaves:", ride.available_seats, ride.passengers)

    ride = svc.cancel_ride(ride.ride_id, driver.user_id)
    print("After cancel:", ride.status)


if __name__ == "__main__":
    main()
