from dataclasses import dataclass


@dataclass
class Credentials:
    api_key: str

    def to_headers(self) -> dict[str]:
        return {"Authorization": self.api_key}
