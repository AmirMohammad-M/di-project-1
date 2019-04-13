from BaseState import BaseState


class MainPageState(BaseState):
    def __init__(self, r, userId):
        self.userId = userId
        self.r = r

    def process(self):
        # fetch list of chats

        print(':create chat: to start a new chat')
        print(':create group: to make a new group')
        print(':contacts: contacts list')
        print(':show chat/group ##: view messages of the specified ##')
        selection = input('Enter command:')

        if selection == 'create chat':
            return CreateChatState(r)
        elif selection == 'create group':
            return CreateGroupState(r)
        elif selection == 'contacts':
            return ContactsListState(r)
        elif selection.startswith('show'):
            cmd = selection.split(' ')
            idx = int(cmd[2])
            if cmd[1] == 'group':
                return ShowChatState(r)
            elif cmd[1] == 'chat':
                return ShowGroupState(r)
