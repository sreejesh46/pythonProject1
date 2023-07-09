book_shop = {}
book_shop['Adventures of Huckleberry Finn'] = 40
book_shop['The Famous Five'] = 15
book_shop['The Adventures of Sherlock Holmes'] = 27
print('Initial book shop details:')
for book in book_shop:
    print(book + ': ' + str(book_shop[book]))
book_shop['Adventures of Huckleberry Finn'] += 5
book_shop['The Famous Five'] -= 3
print('\nUpdated book shop details:')
for book in book_shop:
    print(book + ': ' + str(book_shop[book]))
