phone = input('Enter phone number: ')

# Format the phone number as three groups of 3 digits each
formatted_phone = phone[:3] + '-' + phone[3:6] + '-' + phone[6:]

print("Phone number:", formatted_phone)