import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

creds = ServiceAccountCredentials.from_json_keyfile_dict(
    creds_dict,
    scope
)

client = gspread.authorize(creds)

sheet = client.open("UMBT BOT").sheet1


def save_user(data):
    sheet.append_row([
        data["fio"],
        data["company"],
        data["position"],
        data["telegram"],
        data["email"],
    ])
