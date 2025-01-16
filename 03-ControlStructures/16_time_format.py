def convert_to_12hr_format(time_24hr):
    # Split the time into hours and minutes
    hours, minutes = map(int, time_24hr.split(":"))
    
    # Determine whether it's AM or PM
    if hours >= 12:
        period = "pm"
        if hours > 12:
            hours -= 12
    else:
        period = "am"
        if hours == 0:
            hours = 12  # Midnight case
    
    # Format the time in 12-hour format
    return f"{hours}:{minutes:02d}{period}"

# Read time in 24-hour format from the user
time_24hr = input("Enter time (24-hour format): ")

# Convert and print the time in 12-hour format
time_12hr = convert_to_12hr_format(time_24hr)
print(f"Time in 12-hour format: {time_12hr}")
