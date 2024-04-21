import phonenumbers
from phonenumbers import geocoder, carrier, timezone


print( '*' * 50)

entered_num = input("Please Enter a phone Number: ")

# create phone number object
# None becuse enterde country code
#or enterd country
phone_num = phonenumbers.parse(entered_num, None)

print(phone_num)

# information about lociation
#geocoder

print(geocoder.description_for_number(phone_num, "en"))

#some contryis about phone number and orqnazion
#carieer
print(carrier.name_for_number(phone_num, "en"))


# timezon about the number
print(timezone.time_zones_for_number(phone_num))

