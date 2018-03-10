phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

# step 1 -
print phonebook_dict['Elizabeth']

# step 2 - add a phone
phonebook_dict['Kareem'] = '404-123-1234'

# step 3 - delete Alice
del phonebook_dict['Alice']

# step 4 - change Bob's Phone
phonebook_dict['Bob'] = '404-444-4444'

# step 5 - print the dictionary
print phonebook_dict
