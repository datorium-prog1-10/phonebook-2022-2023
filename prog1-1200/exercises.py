# UZDEVUMS 1
# Izstrāda kodu kas nolasa students.josn failu un
# izvada katra studenta vārdu un uzvārdu šādi:
#
# Name Surname
# Name Surname
# Name Surname
# Name Surname
#...
# Name Surname
import json

fails = open('prog1-1200/students.json', 'r')
vardnica = json.load(fails)
fails.close()

for student in vardnica['Students']:
    print(f"{student['FirstName']} {student['LastName']}")
