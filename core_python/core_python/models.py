# core_python/models.py
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


# -----------------------------
# Helpers
# -----------------------------
def _clean_str(x: Any) -> str:
    return "" if x is None else str(x).strip()


def parse_stops(stops_raw: Any) -> List[str]:
    if stops_raw is None:
        return []
    if isinstance(stops_raw, list):
        return [_clean_str(x) for x in stops_raw if _clean_str(x)]
    if isinstance(stops_raw, str):
        return [p.strip() for p in stops_raw.split("|") if p.strip()]
    s = _clean_str(stops_raw)
    return [s] if s else []


def serialize_stops(stops: List[str]) -> str:
    cleaned = [s.strip() for s in stops if s and s.strip()]
    return "|".join(cleaned)


def parse_offer_data(dados_raw: Any) -> List[str]:
    """
    App Inventor salva 'dados_oferta' como LISTA (global oferta).
    Mas pode existir caso antigo como string; aqui a gente trata ambos.
    """
    if dados_raw is None:
        return []
    if isinstance(dados_raw, list):
        return [_clean_str(x) for x in dados_raw]
    if isinstance(dados_raw, str):
        s = dados_raw.strip()
        return [s] if s else []
    return [_clean_str(dados_raw)] if _clean_str(dados_raw) else []


# -----------------------------
# User (USUARIOS/<user_id>)
# -----------------------------
@dataclass(frozen=True)
class User:
    user_id: str
    name: str
    email: str
    phone: str
    car_model: str = ""
    car_color: str = ""
    plate: str = ""
    stops: List[str] = field(default_factory=list)

    @staticmethod
    def from_firebase(user_id: str, data: Dict[str, Any]) -> "User":
        return User(
            user_id=_clean_str(user_id),
            name=_clean_str(data.get("nome")),
            email=_clean_str(data.get("email")),
            phone=_clean_str(data.get("telefone")),
            car_model=_clean_str(data.get("carro")),
            car_color=_clean_str(data.get("cor")),
            plate=_clean_str(data.get("placa")),
            stops=parse_stops(data.get("paradas")),
        )

    def to_firebase(self) -> Dict[str, Any]:
        return {
            "nome": self.name,
            "email": self.email,
            "telefone": self.phone,
            "carro": self.car_model,
            "cor": self.car_color,
            "placa": self.plate,
            "paradas": serialize_stops(self.stops),
        }


# -----------------------------
# Offer (OFERTAS/<offer_index>)
# -----------------------------
@dataclass
class Offer:
    offer_key: str                 # chave no Firebase (ex: "1", "2", ...)
    offer_id: str = ""             # campo "id"
    available_seats: int = 0       # campo "num_vagas"
    dados_oferta: List[str] = field(default_factory=list)  # LISTA ordenada (igual global oferta)
    driver_user_id: str = ""       # opcional: "id_ofertador" (se você decidir salvar)
    payload: Dict[str, Any] = field(default_factory=dict)  # campos extras

    @staticmethod
    def from_firebase(offer_key: str, data: Dict[str, Any]) -> "Offer":
        raw_seats = data.get("num_vagas", 0)
        try:
            seats = int(raw_seats)
        except (TypeError, ValueError):
            seats = 0

        known = {"id_ofertador", "id", "num_vagas", "dados_oferta"}
        payload = {k: v for k, v in data.items() if k not in known}

        return Offer(
            offer_key=_clean_str(offer_key),
            offer_id=_clean_str(data.get("id")),
            available_seats=seats,
            dados_oferta=parse_offer_data(data.get("dados_oferta")),
            driver_user_id=_clean_str(data.get("id_ofertador")),
            payload=payload,
        )

    def to_firebase(self) -> Dict[str, Any]:
        base: Dict[str, Any] = {
            "id": self.offer_id,
            "num_vagas": int(self.available_seats),
            "dados_oferta": list(self.dados_oferta),
        }

        if self.driver_user_id:
            base["id_ofertador"] = self.driver_user_id

        for k, v in self.payload.items():
            if k not in base:
                base[k] = v

        return base


# -----------------------------
# Firebase root keys
# -----------------------------
@dataclass(frozen=True)
class FirebaseRootKeys:
    USERS: str = "USUARIOS"
    OFFERS: str = "OFERTAS"
    OFFERS_COUNT: str = "Nofertas"
    LAST_OFFER_DAY: str = "dia_ultima_oferta"
