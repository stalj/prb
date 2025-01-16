def time_string(hours, minutes, time_format):
    if time_format == '24':
        # Format hours and minutes with leading zeros for 24-hour format
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        # Determine am/pm suffix
        suffix = 'am' if hours < 12 else 'pm'
        # Convert 0 hour to 12 for 12-hour format
        display_hour = hours % 12 or 12
        return f"{display_hour}:{minutes:02}{suffix}"
    else:
        raise ValueError("Invalid time format. Use '24' or '12'.")

# Testing the function
print(time_string(13, 00, '12'))  # Expected: '15:38'

