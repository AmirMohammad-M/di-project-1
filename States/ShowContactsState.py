from States.AddContactState import AddContactState
from States.BaseState import BaseState


class ShowContactsState(BaseState):
    def __init__(self, r, id):
        self.userId = id
        self.r = r
        self.filter = ''

    def process(self):
        contacts = self.r.smembers(self.userId + ':contacts')
        if not contacts:
            print('No contacts.')
        else:
            for i, phone in enumerate(contacts):
                name = self.r.hget(phone, 'name').decode('ascii')
                if name.startswith(self.filter):
                    print(i + 1, name, phone.decode('ascii'))
        print('\n\n> Enter ADD to add a new contact.')
        print('> Enter BACK to return to chats list.')
        cmd = input('> ')
        if cmd == 'ADD':
            return AddContactState(self.r, self.userId)
        elif cmd.startswith('ADDFILTER '):
            self.filter = cmd.replace('ADDFILTER ', '')
            return self
            # return SearchContactState(self.r, self.userId)
        elif cmd.startswith('RMFILTER'):
            self.filter = ''
            return self
        else:
            from States.MainPageState import MainPageState
            return MainPageState(self.r, self.userId)
