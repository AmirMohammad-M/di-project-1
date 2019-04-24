from States.BaseState import BaseState
from States.AddMemberState import AddMemberState


class ShowMembersState(BaseState):
    def __init__(self, r, id, chatId):
        self.userId = id
        self.r = r
        self.chatId = chatId

    def process(self):
        members = self.r.smembers(self.chatId + ':members')
        if not members:
            print('No Members.')
        else:
            for phone in members:
                name = self.r.hget(phone, 'name').decode('ascii')
                print(name, phone.decode('ascii'))

        print('\n\n> Enter ADD to add a new member.')
        print('> Enter BACK to return to group.')
        cmd = input('> ')
        if cmd == 'ADD':
            return AddMemberState(self.r, self.userId, self.chatId)
        else:
            from States.MainPageState import MainPageState
            return MainPageState(self.r, self.userId)
