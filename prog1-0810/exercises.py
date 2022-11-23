# UZDEVUMS 1
# Izveido programmu kas izvadīs karta studenta V;ārdu un Uzvārdu
# šādā formātā
#
# Name Surname
# Name Surname
# Name Surname
# Name Surname
# ...
# Name Surname
import json

file = open('prog1-0810/students.json', 'r')
data = json.load(file)
file.close()

for student in data['Students']:
    print(f"{student['FirstName']} {student['LastName']}")
