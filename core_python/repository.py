# core_python/repository.py
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict


@dataclass
class JsonRepository:
    """
    Minimal JSON repository used by core_python/services.py.

    Stores a single JSON file with two top-level keys:
      - "firebase": simulates Firebase Realtime Database state
      - "local": simulates TinyDB-like temporary storage
    """
    file_path: str = "core_python/storage.json"

    def _path(self) -> Path:
        return Path(self.file_path)

    def _default_state(self) -> Dict[str, Any]:
        return {
            "firebase": {
                "USUARIOS": {},
                "OFERTAS": {},
                "Nofertas": 0,
                "dia_ultima_oferta": 0,
            },
            "local": {},
        }

    def get_all(self) -> Dict[str, Any]:
        p = self._path()
        if not p.exists():
            state = self._default_state()
            self.save_all(state)
            return state

        try:
            with p.open("r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            data = self._default_state()
            self.save_all(data)

        if not isinstance(data, dict):
            data = self._default_state()
            self.save_all(data)

        # Ensure required keys exist
        data.setdefault("firebase", {})
        data.setdefault("local", {})

        fb = data["firebase"]
        fb.setdefault("USUARIOS", {})
        fb.setdefault("OFERTAS", {})
        fb.setdefault("Nofertas", 0)
        fb.setdefault("dia_ultima_oferta", 0)

        return data

    def save_all(self, data: Dict[str, Any]) -> None:
        p = self._path()
        p.parent.mkdir(parents=True, exist_ok=True)

        with p.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
