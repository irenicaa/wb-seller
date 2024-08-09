from dataclasses import dataclass
from typing import Generator, Optional, Union
from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from . import credentials, request_api


# Request


@dataclass
class PaginatedCardsCursor(DataClassJsonMixin):
    updatedAt: Optional[str] = None
    nmID: Optional[int] = None
    limit: Optional[int] = None


@dataclass
class PaginatedCardsSettingsFilter(DataClassJsonMixin):
    textSearch: Optional[str] = None
    allowedCategoriesOnly: Optional[bool] = True
    tagIDs: Optional[list[str]] = None
    objectIDs: Optional[list[str]] = None
    brands: Optional[list[str]] = None
    imtID: Optional[int] = None
    withPhoto: Optional[int] = None


@dataclass
class PaginatedCardsSettingsAscending(DataClassJsonMixin):
    ascending: Optional[bool] = False


@dataclass
class PaginatedCardsSettings(DataClassJsonMixin):
    sort: Optional[PaginatedCardsSettingsAscending] = None
    filter: Optional[PaginatedCardsSettingsFilter] = None
    cursor: Optional[PaginatedCardsCursor] = None


@dataclass
class PaginatedCards(DataClassJsonMixin):
    settings: Optional[PaginatedCardsSettings] = None


# Response


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetCardsContentResponseResultTags:
    id: Optional[int]
    name: Optional[str]
    color: Optional[str]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetCardsContentResponseResultSizes:
    chrtID: Optional[int]
    techSize: Optional[str]
    skus: Optional[list[str]]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetCardsContentResponseResultCharacteristics:
    id: Optional[int]
    name: Optional[str]
    value: Optional[Union[list[str], int, str, bool, float]]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetCardsContentResponseResultDimensions:
    length: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    square: Optional[int] = None
    isValid: Optional[bool] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetCardsContentResponseResultPhotos:
    big: Optional[str]
    c246x328: Optional[str]
    c516x688: Optional[str]
    square: Optional[str]
    tm: Optional[str]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetCardsContentResponseResultCards:
    nmUUID: Optional[str] = None
    subjectID: Optional[int] = None
    subjectName: Optional[str] = None
    vendorCode: Optional[str] = None
    brand: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    photos: Optional[list[GetCardsContentResponseResultPhotos]] = None
    video: Optional[str] = None
    dimensions: Optional[GetCardsContentResponseResultDimensions] = None
    characteristics: Optional[list[GetCardsContentResponseResultCharacteristics]] = None
    sizes: Optional[list[GetCardsContentResponseResultSizes]] = None
    tags: Optional[list[GetCardsContentResponseResultTags]] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
    nmID: Optional[int] = None
    imtID: Optional[int] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetCardsContentResponseResultPagination:
    updatedAt: Optional[str]
    nmID: Optional[int]
    total: Optional[int]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class GetCardsContentResponseResult:
    cards: Optional[list[GetCardsContentResponseResultCards]]
    cursor: Optional[GetCardsContentResponseResultPagination]


def get_cards(
    credentials: credentials.Credentials,
    data: PaginatedCards,
) -> GetCardsContentResponseResult:

    return request_api.request_api_json(
        "POST",
        "https://content-api.wildberries.ru/content/v2/get/cards/list",
        credentials,
        data,
        response_cls=GetCardsContentResponseResult,
    )


def get_cards_iterative(
    credentials: credentials.Credentials,
    data: PaginatedCards,
) -> Generator[GetCardsContentResponseResult, None, None]:
    while True:
        cards = get_cards(credentials, data)
        if cards.cursor.total < data.settings.cursor.limit:
            break

        yield cards

        data.settings.cursor.updatedAt = cards.cursor.updatedAt
        data.settings.cursor.nmID = cards.cursor.nmID
