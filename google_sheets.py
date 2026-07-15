import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json",
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