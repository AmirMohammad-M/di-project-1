from States.BaseState import BaseState
from States.ShowChatState import ShowChatState
from utils import selectContact
import datetime


class CreateChatState(BaseState):
    def __init__(self, r, id):
        self.userId = id
        self.r = r

    def process(self):
        contact = selectContact(self.userId, self.r)
        chatslistKey = self.userId+'chatslist'

        newChatId = 'PV:' + (self.userId+':'+contact if self.userId <
                             contact else contact + ':'+self.userId)
        self.r.zadd(chatslistKey, newChatId, datetime.time())
        print('Channel Created')
        return ShowChatState(self.r, self.userId)
