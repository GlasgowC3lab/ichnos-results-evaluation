# Imports
import sys
import requests


HEADERS = {"auth-token": "sandbox_token"}
BASE_PAST_RANGE = "https://api.electricitymaps.com/v3/carbon-intensity/past-range"
BASE_STAMP = "YYYY-MM-DDTHH%3A00%3A00.000Z"


def get_ci_data(region, start, end):
    url = f'{BASE_PAST_RANGE}?zone={region}&start={start}&end={end}'
    response = requests.get(url=url, headers=HEADERS)
    data = response.json()
    return data["data"]


def format_date(year, month, day, hour):
    return BASE_STAMP.replace('YYYY', year).replace('MM', month).replace('DD', day).replace('HH', hour)


def process(raw_data):
    data = []

    for entry in raw_data:
        print(entry)
        full_datetime = entry['datetime']
        ci = entry['carbonIntensity']
        
    #   "carbonIntensity": 158,
    #   "datetime": "2026-02-01T01:00:00.000Z",
    # format? date,start,end,actual
    # 2025-01-30,00:00,00:30,5.0

    return data


if __name__ == "__main__":
    arguments = sys.argv[1:]
    data = get_ci_data('GB', format_date('2026', '02', '01', '00'), format_date('2026', '02', '04', '23'))
    processed_data = process(data)
    print(processed_data)
