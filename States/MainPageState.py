from States.BaseState import BaseState
from utils import printChatsList


class MainPageState(BaseState):
    def __init__(self, r, userId):
        self.userId = userId
        self.r = r

    def process(self):
        chatids = self.r.zrevrange(self.userId+':chatslist', 0, 10)
        # chats = list(map(lambda id: self.r.chatids))
        # printChatsList(chats)

        if not chatids:
            print('Your chats list is empty.')
            print('\n')
        print(':create chat: to start a new chat')
        print(':create group: to make a new group')
        print(':contacts: contacts list')
        print(':open ##: view messages of the specified ##')
        selection = input('Enter command:')

        if selection == 'create chat':
            return CreateChatState(r)
        elif selection == 'create group':
            return CreateGroupState(r)
        elif selection == 'contacts':
            return ContactsListState(r)
        elif selection.startswith('open'):
            cmd = selection.split(' ')
            idx = int(cmd[1])
            if cmd[1] == 'group':
                return ShowChatState(r)
            elif cmd[1] == 'chat':
                return ShowGroupState(r)


def resolveChatId(id, r):
    chat = r.get(id)
