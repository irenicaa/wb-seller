import datetime
import os

import dotenv

import credentials, http_error, cards_list

if __name__ == "__main__":
    dotenv.load_dotenv()
    wb_credentials = credentials.Credentials(
        os.getenv("TEST2"),
    )
    data = cards_list.PaginatedCards(
        settings=cards_list.PaginatedCardsSettings(
            cursor=cards_list.PaginatedCardsCursor(limit=2),
            filter=cards_list.PaginatedCardsSettingsFilter(withPhoto=-1),
        )
    )
    print(data.to_json())
    status = cards_list.get_cards_iterative(wb_credentials, data)
    print("status", list(status))
