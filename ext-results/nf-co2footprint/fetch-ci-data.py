# Imports
import sys
import requests


HEADERS = {"auth-token": "api_token"}
BASE_PAST_RANGE = "https://api.electricitymaps.com/v3/carbon-intensity/past-range"
BASE_STAMP_START = "YYYY-MM-DD+00%3A00"
BASE_STAMP_END = "YYYY-MM-DD+23%3A59"


def get_ci_data(region, start, end):
    url = f'{BASE_PAST_RANGE}?zone={region}&start={start}&end={end}&temporalGranularity=5_minutes'
    response = requests.get(url=url, headers=HEADERS)
    data = response.json()
    return data["data"]


def format_date_start(parts):
    year, month, day = parts
    return BASE_STAMP_START.replace('YYYY', year).replace('MM', month).replace('DD', day)


def format_date_end(parts):
    year, month, day = parts
    return BASE_STAMP_END.replace('YYYY', year).replace('MM', month).replace('DD', day)


def process(raw_data):
    data = []

    for entry in raw_data:
        full_datetime = entry['datetime']
        date = full_datetime.split('T')[0].strip()
        start = full_datetime.split('T')[1][:-8]
        ci = str(entry['carbonIntensity'])
        data.append((date, start, ci))

    return data


if __name__ == "__main__":
    # uncomment one at a time, prevent calling the API too often
    gb_dates = [
        # [('2026', '01', '28'), ('2026', '01', '29'), ('2026', '01', '30')],
        # [('2026', '02', '10'), ('2026', '02', '11'), ('2026', '02', '12')],
        # [('2026', '02', '27'), ('2026', '02', '28')],
    ]

    de_dates = [
        # [('2025', '11', '17'), ('2025', '11', '18'), ('2025', '11', '19'), ('2025', '11', '20'), ('2025', '11', '21'), ('2025', '11', '22'), ('2025', '11', '23'), ('2025', '11', '24')],
        # [('2026', '02', '07'), ('2026', '02', '08'), ('2026', '02', '09')],
        # [('2026', '02', '20'), ('2026', '02', '21'), ('2026', '02', '22'), ('2026', '02', '23'), ('2026', '02', '24')],
        # [('2026', '03', '05'), ('2026', '03', '06'), ('2026', '03', '07')]
    ]

    for dates in gb_dates:
        dates_data = []
        for day in dates:
            day_data = get_ci_data('GB', format_date_start(day), format_date_end(day))
            processed_day = process(day_data)
            dates_data.extend(processed_day)

        with open(f'ci/gb-{'-'.join(dates[0])}-{'-'.join(dates[-1])}.csv', 'w') as file:
            file.write('date,start,actual\n')
            for entry in dates_data:
                file.write(f"{','.join(entry)}\n")

    for dates in de_dates:
        dates_data = []
        for day in dates:
            day_data = get_ci_data('DE', format_date_start(day), format_date_end(day))
            processed_day = process(day_data)
            dates_data.extend(processed_day)

        with open(f'ci/de-{'-'.join(dates[0])}-{'-'.join(dates[-1])}.csv', 'w') as file:
            file.write('date,start,actual\n')
            for entry in dates_data:
                file.write(f"{','.join(entry)}\n")
