def selectContact(userId, r):
    contacts = list(r.smembers(userId + ':contacts'))
    if len(contacts) == 0:
        print('Your contacts list is empty.')
    else:
        for i, c in enumerate(contacts):
            name = r.hget(c.decode('ascii'), 'name').decode('ascii')
            print(i + 1, name, c.decode('ascii'))
        selection = input('Enter contact idx:')
        return contacts[int(selection) - 1].decode('ascii')
    return None


def selectContacts(userId, r):
    contacts = list(r.smembers(userId + ':contacts'))
    if len(contacts) == 0:
        print('Your contacts list is empty.')
    else:
        for i, c in enumerate(contacts):
            name = r.hget(c.decode('ascii'), 'name').decode('ascii')
            print(i + 1, name, c.decode('ascii'))
        selection = input('Enter contact ids(comma separated):')
        res = set()
        for idx in selection.split(','):
            res.add(contacts[int(idx) - 1].decode('ascii'))
        return res
    return res
