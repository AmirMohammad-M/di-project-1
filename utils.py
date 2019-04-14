def selectContact(userId, r):
    contacts = r.get(userId+':contacts')

    for c in contacts:
        print(c)

    selection = input('Enter contact idx:')
    return contacts[selection]


def printChatsList(chats):
    for c in chats:
        print(c)
