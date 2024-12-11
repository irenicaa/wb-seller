from dataclasses import dataclass
from typing import Generator, Optional, Union
from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from . import credentials, request_api


# Request


@dataclass
class StocksData(DataClassJsonMixin):
    sku: Optional[str] = None
    amount: Optional[int] = None


@dataclass
class Stocks(DataClassJsonMixin):
    stocks: Optional[StocksData] = None


def update_stocks(
    credentials: credentials.Credentials,
    data: Stocks,
    warehouse_id: int,
) -> None:

    return request_api.request_api_raw(
        "PUT",
        "https://marketplace-api.wildberries.ru/api/v3/stocks/" + str(warehouse_id),
        credentials,
        data.to_json(),
    )
