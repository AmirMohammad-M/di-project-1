import time

from States.BaseState import BaseState
from States.ShowChatState import ShowChatState
from utils import selectContact


class CreateChatState(BaseState):
    def __init__(self, r, id):
        self.userId = id
        self.r = r

    def process(self):
        from States.MainPageState import MainPageState
        contact = selectContact(self.userId, self.r)
        if not contact:
            return MainPageState(self.r, self.userId)

        chatslistKey = self.userId + ':chatslist'
        contactsChatlistKey = contact + ':chatslist'
        newChatId = 'PV:' + (
            (self.userId + ':' + contact) if int(self.userId) < int(contact) else (contact + ':' + self.userId))

        self.r.zadd(chatslistKey, {newChatId: int(time.time() * 1000)})
        # TODO Bug Or Feature?
        self.r.zadd(contactsChatlistKey, {newChatId: 0})
        self.r.hset(newChatId, 'lastSeenByOthers', int(time.time() * 1000))
        self.r.set(self.userId+':'+newChatId+':lastSeen', 0)
        print('Chat Created')
        return ShowChatState(self.r, self.userId, newChatId)
