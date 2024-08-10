import datetime
import os

import dotenv

import credentials, http_error, v3_supplies

if __name__ == "__main__":
    dotenv.load_dotenv()
    wb_credentials = credentials.Credentials(
        os.getenv("AUTHORIZATION"),
    )
    data = v3_supplies.Supply(name="test")
    print(data.to_json())
    status = v3_supplies.create_supply(wb_credentials, data)
    print("status", status)
