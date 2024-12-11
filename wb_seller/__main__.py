import datetime
import os

import dotenv

from . import credentials, update_stocks

if __name__ == "__main__":
    dotenv.load_dotenv()
    wb_credentials = credentials.Credentials(
        os.getenv("AUTHORIZATION"),
    )

    data = update_stocks.Stocks(
        stocks=[
            update_stocks.StocksData(
                sku="DATA",
                amount=1,
            )
        ]
    )

    warehouse_id = os.getenv("WAREHOUSE_ID")
    update_stocks.update_stocks(wb_credentials, data, warehouse_id)
