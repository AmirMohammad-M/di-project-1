from BaseState import BaseState


class MainPageState(BaseState):
    def __init__(self, id):
        self.userId = id

    def process(self):
        # fetch list of chats

        print(':create chat: to start a new chat')
        print(':create group: to make a new group')
        print(':contacts: contacts list')
        print(':show chat/group ##: view messages of the specified ##')
        selection = input('Enter command:')

        if selection == 'create chat':
            return CreateChatState()
        elif selection == 'create group':
            return CreateGroupState()
        elif selection == 'contacts':
            return ContactsListState()
        elif selection.startswith('show'):
            cmd = selection.split(' ')
            idx = int(cmd[2])
            if cmd[1] == 'group':
                return
            elif cmd[1] == 'chat':
                return
