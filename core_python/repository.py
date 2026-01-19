import json
from pathlib import Path
from typing import Dict, Any



class JsonRepository:
    """
    Persistência simples para demonstrar lógica do sistema.
    Não substitui Firebase; serve como base de portfólio para rodar localmente.
    """

    def __init__(self, path: str = "core_python/data.json"):
        self.path = Path(path)
        if not self.path.exists():
            self._write({"users": {}, "rides": {}})

    def _read(self) -> Dict[str, Any]:
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _write(self, data: Dict[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def get_all(self) -> Dict[str, Any]:
        return self._read()

    def save_all(self, data: Dict[str, Any]) -> None:
        self._write(data)
