def selectContact(userId, r):
    contacts = list(r.smembers(userId + ':contacts'))
    if len(contacts) == 0:
        print('Your contacts list is empty.')
    else:
        for i, c in enumerate(contacts):
            print(i + 1, c.decode('ascii'))
        selection = input('Enter contact idx:')
        return contacts[int(selection) - 1].decode('ascii')
