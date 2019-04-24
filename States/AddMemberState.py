import time
from States.BaseState import BaseState
from utils import selectContact


class AddMemberState(BaseState):
    def __init__(self, r, id, chatId):
        self.userId = id
        self.r = r
        self.chatId = chatId

    def process(self):
        member = selectContact(self.userId, self.r)
        if not member:
            print('No user with this number exists!')
        else:
            if self.r.sadd(self.chatId + ':members', member):
                print('Contact Added Successfully.')
                self.r.zadd(member+':chatslist',
                            {self.chatId: int(time.time() * 1000)})
                self.r.set(member+':'+self.chatId+':lastSeen', 0)
            else:
                print('Member exists.')
        from States.ShowMembersState import ShowMembersState
        return ShowMembersState(self.r, self.userId, self.chatId)
