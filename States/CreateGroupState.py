import time
from States.BaseState import BaseState
from States.ShowGroupState import ShowGroupState
from utils import selectContacts


class CreateGroupState(BaseState):
    def __init__(self, r, id):
        self.userId = id
        self.r = r

    def process(self):
        print('Select members')
        members = selectContacts(self.userId, self.r)
        members.add(self.userId)

        name = input('Enter a name for the group:')
        newGroupId = 'GP:' + str(int(time.time() * 1000) %
                                 (365 * 24 * 60 * 60 * 1000))
        self.r.hset(newGroupId, 'name', name)
        self.r.hset(newGroupId, 'creator', self.userId)
        self.r.hset(newGroupId, 'lastSeenByOthers', 0)
        self.r.sadd(newGroupId+':members', *members)
        for member in members:
            self.r.zadd(member+':chatslist',
                        {newGroupId: int(time.time() * 1000)})
            self.r.set(member+':'+newGroupId+':lastSeen', 0)
        print('Group created.')

        return ShowGroupState(self.r, self.userId, newGroupId)
