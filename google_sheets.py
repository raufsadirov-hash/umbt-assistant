import os
import json
import gspread
from google.oauth2.service_account import Credentials


sheet = None


def get_sheet():
    global sheet

    if sheet is None:
        print("Подключаюсь к Google Sheets...")

        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]

        creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

        creds = Credentials.from_service_account_info(
            creds_dict,
            scopes=scope
        )

        client = gspread.authorize(creds)

        sheet = client.open("UMBT BOT").sheet1

        print("Google Sheets подключен!")

    return sheet


def save_user(data):
    sh = get_sheet()

    sh.append_row([
        data["fio"],
        data["company"],
        data["position"],
        data["telegram"],
        data["email"],
    ])
