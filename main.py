import csv


# CSV (ish) file: each line represents a duration (two dates)
def load_data(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows

# Load the data by converting each line to a timedelta (duration) value
def get_duration(time_list):
    
# Add the list of durations together
# Convert as needed (hours, minutes)
# Return final duration


print(load_data("dates.csv"))
