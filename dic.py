phonebook = {
    'Zayn': '4564565445',
    'Harry': '344242434',
    'Charlie': '55579012',
    'David': '6974335353',
    'Mathew': '56332434'
}
sorted_keys = sorted(phonebook.keys())
for key in sorted_keys:
    print(key + ': ' + phonebook[key])

