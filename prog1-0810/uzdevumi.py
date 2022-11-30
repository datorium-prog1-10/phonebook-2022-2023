# UZDEVUMS 1: izveido programmu kas izvadīs:
# FirstName LastName (Grade)
# FirstName LastName (Grade)
# FirstName LastName (Grade)
# ...
# FirstName LastName (Grade)
# FirstName LastName (Grade)

import json

file = open('prog1-0810/students.json', 'r')
data = json.load(file)
file.close()

for s in data['Students']:
    print(f"{s['FirstName']} {s['LastName']} ({s['Grade']})")

# UZDEVUMS 2 izveido programmu
# kas aprēķinās visu studentu vidējo atzīmi

#Risinājums 1
grade_sum = 0
for s in data['Students']:
    grade_sum += int(s['Grade'])

average_grade = grade_sum / len(data['Students'])
print(f"Student count is {len(data['Students'])}")
print(f"Average grade is {average_grade}")

#Risinājums 2
grade_list = []
for s in data['Students']:
    grade_list.append(int(s['Grade']))
print(f"Student count is {len(grade_list)}")
print(f"Average grade is {sum(grade_list) / len(grade_list)}")

# UZDEVUMS 3 izveido programmu
# kas aprēķinās katra dzimuma vidējo atzīmi
female_grade_list = []
male_grade_list = []
other_grade_list = []

for s in data['Students']:
    if s['Gender'] == 'Female':
        female_grade_list.append(int(s['Grade']))
    elif s['Gender'] == 'Male':
        male_grade_list.append(int(s['Grade']))
    else:
        other_grade_list.append(int(s['Grade']))

print(f"Female count: {len(female_grade_list)}")
print(f"Female grade average: {sum(female_grade_list) / len(female_grade_list)}")
print(f"Male count: {len(male_grade_list)}")
print(f"Male grade average: {sum(male_grade_list) / len(male_grade_list)}")
#print(f"Other count: {len(other_grade_list)}")
#print(f"Other grade average: {sum(other_grade_list) / len(other_grade_list)}")