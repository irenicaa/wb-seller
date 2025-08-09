import datetime
import os

import dotenv

from . import credentials, set_price_discount

if __name__ == "__main__":
    dotenv.load_dotenv()
    wb_credentials = credentials.Credentials(
        os.getenv("PRICE"),
    )

    data = set_price_discount.Price(
        data=[
            set_price_discount.PriceData(
                nmID=123456,
                discount=40,
            )
        ]
    )

    warehouse_id = os.getenv("WAREHOUSE_ID")
    set_price_discount.update_price(wb_credentials, data)
