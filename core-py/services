# core_python/services.py
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any, Dict, List, Optional, Tuple

from core_python.models import FirebaseRootKeys, Offer, User
from core_python.repository import JsonRepository


@dataclass(frozen=True)
class OfferInput:
    """
    Minimum fields to create an offer in a Firebase-compatible shape.

    This matches the App Inventor structure:
      OFERTAS/<Nofertas> = {
        "id": <driver_id>,
        "num_vagas": <int>,
        "dados_oferta": <list[str]> or <str>,
        "id_ofertador": <driver_id> (optional but recommended)
      }
    """
    driver_id: str
    seats: int
    departure_label: str          # e.g., "Unifal", "Downtown", "Campus"
    destination_label: str        # e.g., "Rodoviária"
    hour: str                     # "08"
    minute: str                   # "30"
    stops_text: str               # "A|B|C" or any readable string
    car_model: str
    car_color: str
    plate: str


class UniCarService:
    def __init__(self, repo: JsonRepository):
        self.repo = repo
        self.keys = FirebaseRootKeys()

    # =========================================================
    # Internal persistence helpers
    # =========================================================
    def _ensure_schema(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data.setdefault("firebase", {})
        fb = data["firebase"]
        fb.setdefault(self.keys.USERS, {})         # "USUARIOS"
        fb.setdefault(self.keys.OFFERS, {})        # "OFERTAS"
        fb.setdefault(self.keys.OFFERS_COUNT, 0)   # "Nofertas"
        fb.setdefault(self.keys.LAST_OFFER_DAY, 0) # "dia_ultima_oferta"

        data.setdefault("local", {})               # TinyDB-like
        return data

    def _load(self) -> Dict[str, Any]:
        data = self.repo.get_all()
        if not isinstance(data, dict):
            data = {}
        return self._ensure_schema(data)

    def _save(self, data: Dict[str, Any]) -> None:
        self.repo.save_all(data)

    def _today_day_of_month(self) -> int:
        return date.today().day

    def _parse_int(self, value: Any, default: int = 0) -> int:
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    # =========================================================
    # Users (USUARIOS/<user_id>)
    # =========================================================
    def upsert_user(self, user: User) -> User:
        data = self._load()
        fb = data["firebase"]
        fb[self.keys.USERS][user.user_id] = user.to_firebase()
        self._save(data)
        return user

    def get_user(self, user_id: str) -> Optional[User]:
        data = self._load()
        fb = data["firebase"]
        payload = fb[self.keys.USERS].get(str(user_id))
        if not isinstance(payload, dict):
            return None
        return User.from_firebase(str(user_id), payload)

    # =========================================================
    # Offers (OFERTAS/<offer_key>)
    # =========================================================
    def create_offer(self, offer_in: OfferInput) -> Offer:
        data = self._load()
        fb = data["firebase"]

        current_n = self._parse_int(fb.get(self.keys.OFFERS_COUNT), 0)
        new_n = current_n + 1

        fb[self.keys.OFFERS_COUNT] = new_n
        fb[self.keys.LAST_OFFER_DAY] = self._today_day_of_month()

        seats = max(self._parse_int(offer_in.seats, 0), 0)

        details: List[str] = [
            f"Departure: {offer_in.departure_label}, Destination: {offer_in.destination_label}",
            f"Time: {offer_in.hour}:{offer_in.minute}",
            f"Stops: {offer_in.stops_text}",
            f"Car: {offer_in.car_model}",
            f"Color: {offer_in.car_color}",
            f"Plate: {offer_in.plate}",
        ]

        offer = Offer(
            offer_key=str(new_n),
            driver_user_id=str(offer_in.driver_id),
            offer_id=str(offer_in.driver_id),      # App Inventor field "id" = driver id
            available_seats=seats,
            ride_text="",
            payload={},
        )

        # Keep Firebase compatibility: store "dados_oferta" as list of strings
        firebase_payload = offer.to_firebase()
        firebase_payload["dados_oferta"] = details
        firebase_payload["id_ofertador"] = str(offer_in.driver_id)

        fb[self.keys.OFFERS][str(new_n)] = firebase_payload
        self._save(data)

        return Offer.from_firebase(str(new_n), firebase_payload)

    def list_available_offers(self) -> List[Offer]:
        data = self._load()
        fb = data["firebase"]
        offers_raw = fb.get(self.keys.OFFERS)

        if not isinstance(offers_raw, dict):
            return []

        offers: List[Offer] = []
        for offer_key, payload in offers_raw.items():
            if not isinstance(payload, dict):
                continue
            o = Offer.from_firebase(str(offer_key), payload)
            if o.available_seats > 0:
                offers.append(o)

        offers.sort(key=lambda x: self._parse_int(x.offer_key, 10**9))
        return offers

    def get_offer(self, offer_key: str) -> Optional[Offer]:
        data = self._load()
        fb = data["firebase"]
        payload = fb[self.keys.OFFERS].get(str(offer_key))
        if not isinstance(payload, dict):
            return None
        return Offer.from_firebase(str(offer_key), payload)

    # =========================================================
    # Selection (TinyDB-like local storage)
    # =========================================================
    def select_offer(self, offer_key: str) -> Offer:
        data = self._load()
        fb = data["firebase"]
        local = data["local"]

        payload = fb[self.keys.OFFERS].get(str(offer_key))
        if not isinstance(payload, dict):
            raise ValueError("offer not found")

        offer = Offer.from_firebase(str(offer_key), payload)

        local["offer_key"] = offer.offer_key
        local["id_ofertador"] = payload.get("id_ofertador") or offer.driver_user_id or offer.offer_id
        local["dados_oferta"] = payload.get("dados_oferta", [])
        local["num_vagas"] = offer.available_seats

        self._save(data)
        return offer

    def confirm_selected_offer(self) -> Offer:
        data = self._load()
        fb = data["firebase"]
        local = data["local"]

        offer_key = local.get("offer_key")
        if not offer_key:
            raise ValueError("no offer selected")

        payload = fb[self.keys.OFFERS].get(str(offer_key))
        if not isinstance(payload, dict):
            raise ValueError("offer not found")

        offer = Offer.from_firebase(str(offer_key), payload)

        if offer.available_seats <= 0:
            raise ValueError("no available seats")

        offer.available_seats -= 1
        updated_payload = payload.copy()
        updated_payload["num_vagas"] = int(offer.available_seats)

        fb[self.keys.OFFERS][str(offer_key)] = updated_payload
        local["num_vagas"] = offer.available_seats

        self._save(data)
        return Offer.from_firebase(str(offer_key), updated_payload)

    # =========================================================
    # WhatsApp message builder (UI integration)
    # =========================================================
    def build_whatsapp_message(self, passenger_name: str, pickup_point: str) -> str:
        data = self._load()
        local = data["local"]

        raw_details = local.get("dados_oferta", [])
        if isinstance(raw_details, list):
            details = [str(x).strip() for x in raw_details if str(x).strip()]
        else:
            details = [str(raw_details).strip()] if str(raw_details).strip() else []

        lines: List[str] = []
        lines.append(f"Hello, this is {passenger_name}.")
        lines.append("I would like to join the carpool.")

        pp = (pickup_point or "").strip()
        if pp and pp.lower() != "unifal":
            lines.append(f"Pickup point: {pp}")

        if details:
            lines.append("")
            lines.append("Offer details:")
            for item in details:
                lines.append(f"- {item}")

        return "\n".join(lines).strip()

    # =========================================================
    # Convenience views (ListView-like)
    # =========================================================
    def offers_to_list_strings(self, offers: List[Offer]) -> List[str]:
        result: List[str] = []
        for o in offers:
            title = o.payload.get("title")
            if not title and o.ride_text:
                title = o.ride_text
            if not title:
                title = f"Offer {o.offer_key}"
            result.append(f"[{o.offer_key}] {title} | Seats: {o.available_seats}")
        return result
