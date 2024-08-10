from dataclasses import dataclass
from typing import Generator, Optional
from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

import credentials, request_api

# Request

@dataclass
class Supply(DataClassJsonMixin):
    name: Optional[str] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetNewSupplyResult:
    id: str


def create_supply(
    credentials: credentials.Credentials,
    data: Supply,
) -> GetNewSupplyResult:
    return request_api.request_api_json(
        "POST",
        "https://marketplace-api.wildberries.ru/api/v3/supplies",
        credentials,
        data,
        response_cls=GetNewSupplyResult,
    )
