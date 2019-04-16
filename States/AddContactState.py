from States.BaseState import BaseState


class AddContactState(BaseState):
    def __init__(self, r, id):
        self.userId = id
        self.r = r

    def process(self):
        phone = input('Enter phone number:')
        contactName = self.r.hget(phone, 'name').decode('ascii')
        if not contactName:
            print('No user with this number exists!')
        else:
            if self.r.sadd(self.userId + ':contacts', phone):
                print('Contact Added Successfully.')
            else:
                print('Contact not added.')

        from States.ShowContactsState import ShowContactsState
        return ShowContactsState(self.r, self.userId)
