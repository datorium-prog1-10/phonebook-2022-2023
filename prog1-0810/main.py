contacts = []

while(True):
    response = input('(1)add contact (2)print contacts (3)exit: ')
    if response == '1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_phone = input('Phone: ')
        person_email = input('Email: ')

        person_contact = {
            'name': person_name,
            'surname': person_surname,
            'phone': person_phone,
            'email': person_email
        }
        contacts.append(person_contact)

    elif response == '2':
        for contact in contacts:
            print("---CONTACT---")
            print(f"{contact['name']} {contact['surname']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")        
        
    elif response == '3':
        print('Bye bye!')
        exit()
    else:
        print('Please respond with 1, 2 or 3')

#UZDEVUMS
#Izvadīt kontaktus šādā formātā
#---CONTACT---
#Anna Bērziņa
#Phone: +371 65498798
#Email: ab@somemail.com
#---CONTACT---
#Oskars Gudrais
#Phone: +371 9645785123
#Email: og@somemail.com