from dataclasses import dataclass
from typing import Generator, Optional
from dataclasses_json import Undefined, dataclass_json

from . import credentials, request_api

# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetNewOrdersResponseResultAddress:
    fullAddress: str
    longitude: float
    latitude: float


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetNewOrdersResponseResult:
    address: Optional[GetNewOrdersResponseResultAddress]
    # ddate: Optional[str]
    # dTimeFrom: str
    # dTimeTo: str
    requiredMeta: list[str]
    deliveryType: str
    scanPrice: Optional[str]
    orderUid: str
    article: str
    colorCode: str
    rid: str
    createdAt: str
    offices: list[str]
    skus: list[str]
    id: int
    warehouseId: int
    nmId: int
    chrtId: int
    price: int
    convertedPrice: int
    currencyCode: int
    convertedCurrencyCode: int
    cargoType: int
    isZeroOrder: bool


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetNewOrdersResponseResultWrapper:
    orders: list[GetNewOrdersResponseResult]


def get_orders(
    credentials: credentials.Credentials,
) -> GetNewOrdersResponseResultWrapper:
    return request_api.request_api_json(
        "GET",
        "https://marketplace-api.wildberries.ru/api/v3/orders/new",
        credentials,
        None,
        response_cls=GetNewOrdersResponseResultWrapper,
    )
