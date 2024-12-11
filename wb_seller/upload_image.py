from dataclasses import dataclass
from typing import Generator, Optional, Any
from dataclasses_json import Undefined, dataclass_json, DataClassJsonMixin

from . import credentials, request_api


def upload_image(
    credentials: credentials.Credentials,
    image_filename: str,
    image_number: int,
    sku: str,
) -> None:

    additional_headers = {"X-Photo-Number": str(image_number), "X-Nm-Id": sku}

    with open(image_filename, "rb") as image_file:
        files = {"uploadfile": image_file}
        return request_api.request_api_files(
            "POST",
            "https://content-api.wildberries.ru/content/v3/media/file",
            credentials,
            files,
            additional_headers=additional_headers,
        )
