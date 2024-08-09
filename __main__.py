import datetime
import os

import dotenv

import credentials, http_error, orders_new

if __name__ == "__main__":
    dotenv.load_dotenv()
    ozon_credentials = credentials.Credentials(
        os.getenv("TEST"),
    )
    status = orders_new.get_orders(
        ozon_credentials,
    )
    print("status", status)
