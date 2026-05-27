import csv
from datetime import datetime
from math import floor


# CSV (ish) file: each line represents a duration (two dates)
#
def load_data(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


# Load the data by converting each line to a timedelta (duration) value
def get_duration(time_list):
    start = datetime.strptime(time_list["start"], "%H:%M")
    stop = datetime.strptime(time_list["stop"], "%H:%M")
    duration = stop - start
    return duration.total_seconds() / 60


# Add the list of durations together
def get_total_minutes(duration_list):
    total_minutes = 0
    for time_list in duration_list:
        total_minutes += get_duration(time_list)
    return total_minutes


# Convert as needed (hours, minutes)
def convert_minutes(minutes):
    formatted_time = ""
    if minutes > 60:
        hours = floor(minutes / 60)
        mins = round(minutes % 60)
        formatted_time = f"{hours}:{mins}"
    else:
        formatted_time = f"0:{round(minutes)}"
    return formatted_time


# Return final duration

if __name__ == "__main__":
    time_list = load_data("dates.csv")
    total_minutes = get_total_minutes(time_list)
    timestamp = convert_minutes(total_minutes)
    print(timestamp)
