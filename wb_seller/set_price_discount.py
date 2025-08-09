from dataclasses import dataclass
from typing import Generator, Optional, Union
from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from . import credentials, request_api


# Request


@dataclass
class PriceData(DataClassJsonMixin):
    nmID: Optional[int] = None
    price: Optional[int] = None
    discount: Optional[int] = None


@dataclass
class Price(DataClassJsonMixin):
    data: Optional[list[PriceData]] = None


def update_price(
    credentials: credentials.Credentials,
    data: Price,
) -> None:

    return request_api.request_api_raw(
        "POST",
        "https://discounts-prices-api.wildberries.ru/api/v2/upload/task",
        credentials,
        data.to_json(),
    )
