import datetime
import os

import dotenv

import credentials, upload_image

if __name__ == "__main__":
    dotenv.load_dotenv()
    wb_credentials = credentials.Credentials(
        os.getenv("AUTHORIZATION"),
    )

    image_filename = "file_name"
    upload_image.upload_image(wb_credentials, image_filename, 1, "sku_id")
