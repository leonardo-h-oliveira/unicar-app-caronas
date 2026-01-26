# core_python/models.py
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# -----------------------------
# Helpers (paradas)
# -----------------------------
def parse_stops(stops_raw: Any) -> List[str]:
    """
    No seu app, 'paradas' pode vir como string tipo:
      "Praça Central|Rodoviária"
    ou já como lista, dependendo de como foi salvo.
    """
    if stops_raw is None:
        return []
    if isinstance(stops_raw, list):
        return [str(x).strip() for x in stops_raw if str(x).strip()]
    if isinstance(stops_raw, str):
        # padrão que você usou no exemplo: "A|B|C"
        return [p.strip() for p in stops_raw.split("|") if p.strip()]
    # fallback
    return [str(stops_raw).strip()] if str(stops_raw).strip() else []


def serialize_stops(stops: List[str]) -> str:
    """
    Salva no formato compatível com seu exemplo do Firebase:
      "A|B|C"
    """
    cleaned = [s.strip() for s in stops if s and s.strip()]
    return "|".join(cleaned)


# -----------------------------
# User (USUARIOS/<user_id>)
# -----------------------------
@dataclass(frozen=True)
class User:
    """
    Representa: USUARIOS/<user_id>

    Campos vistos no seu modelo:
      nome, email, telefone, carro, cor, placa, paradas
    """
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
            user_id=str(user_id),
            name=str(data.get("nome", "")),
            email=str(data.get("email", "")),
            phone=str(data.get("telefone", "")),
            car_model=str(data.get("carro", "")),
            car_color=str(data.get("cor", "")),
            plate=str(data.get("placa", "")),
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
    """
    Representa: OFERTAS/<offer_index>

    Pelo print do seu App Inventor, você salva algo como:
      {
        "id": <global id>,
        "num_vagas": <texto da caixa>,
        "dados_oferta": <global oferta>   # texto montado para lista
      }

    Além disso, no seu fluxo você também precisa:
      - identificar o ofertador (id_ofertador) em algum lugar
      - armazenar paradas/horário/rota (pode estar dentro de 'dados_oferta' ou separado)
    """
    offer_key: str  # chave no Firebase (ex: "1", "2", "3"...)
    driver_user_id: str = ""  # id_ofertador (se você salvar isso junto)
    offer_id: str = ""        # campo "id" do dicionário
    available_seats: int = 0  # campo "num_vagas"
    ride_text: str = ""       # campo "dados_oferta"
    payload: Dict[str, Any] = field(default_factory=dict)  # extra fields (se você quiser evoluir)

    @staticmethod
    def from_firebase(offer_key: str, data: Dict[str, Any]) -> "Offer":
        """
        Converte do dicionário do Firebase para Offer.
        """
        # num_vagas pode vir como string no App Inventor
        raw_seats = data.get("num_vagas", 0)
        try:
            seats = int(raw_seats)
        except (TypeError, ValueError):
            seats = 0

        return Offer(
            offer_key=str(offer_key),
            driver_user_id=str(data.get("id_ofertador", "")),
            offer_id=str(data.get("id", "")),
            available_seats=seats,
            ride_text=str(data.get("dados_oferta", "")),
            payload={k: v for k, v in data.items() if k not in {"id_ofertador", "id", "num_vagas", "dados_oferta"}},
        )

    def to_firebase(self) -> Dict[str, Any]:
        """
        Converte Offer para o formato que você salva no Firebase.
        Mantém compatibilidade com:
          id, num_vagas, dados_oferta
        E permite campos extras em payload.
        """
        base = {
            "id": self.offer_id,
            "num_vagas": int(self.available_seats),
            "dados_oferta": self.ride_text,
        }
        if self.driver_user_id:
            base["id_ofertador"] = self.driver_user_id

        # campos extras (se você decidir guardar mais coisa separada no futuro)
        for k, v in self.payload.items():
            if k not in base:
                base[k] = v

        return base


# -----------------------------
# Firebase "root" helpers
# -----------------------------
@dataclass(frozen=True)
class FirebaseRootKeys:
    USERS: str = "USUARIOS"
    OFFERS: str = "OFERTAS"
    OFFERS_COUNT: str = "Nofertas"
    LAST_OFFER_DAY: str = "dia_ultima_oferta"
