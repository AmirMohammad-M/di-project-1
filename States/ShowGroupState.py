import time
from States.BaseState import BaseState


class ShowGroupState(BaseState):
    def __init__(self, r, userId, chatId):
        self.userId = userId
        self.r = r
        self.chatId = chatId

    def process(self):
        print('\n\n Type SEND and start writing text you want to send.')
        print('\n Enter BACK to return to menu.\n')

        messages = self.r.zrange(
            self.chatId + ':messages', 0, 10, withscores=True)
        othersLastSeen = int(self.r.hget(
            self.chatId, 'lastSeenByOthers').decode('ascii'))
        myLastSeen = int(self.r.get(
            self.userId+':'+self.chatId+':lastSeen').decode('ascii'))
        if len(messages) == 0:
            print('No messages.')
        else:
            # update last seen if last message is not yours
            for m, t in messages:

                sender = self.r.hget(m.decode('ascii'), 'from').decode('ascii')
                tab = ''
                seenStatus = ''
                newStatus = ''
                if sender == self.userId:
                    tab = '\t\t\t'
                    if t > othersLastSeen:
                        seenStatus = '[UNSEEN] '
                else:
                    if t > myLastSeen:
                        newStatus = ' [NEW]'
                text = self.r.hget(m.decode('ascii'), 'text').decode('ascii')
                print(tab + seenStatus + text + newStatus)
            else:
                if not sender == self.userId:
                    self.r.hset(self.chatId, 'lastSeenByOthers',
                                int(time.time() * 1000))

        self.r.set(self.userId+':'+self.chatId +
                   ':lastSeen', int(time.time() * 1000))

        inp = input('\n\n> ')
        if inp.startswith('SEND '):
            sTime = int(time.time() * 1000)  # Send Time msec
            text = inp.replace('SEND ', '', 1)
            newMsgId = 'MSG' + str(sTime % (365 * 24 * 60 * 60 * 1000))
            self.r.hset(newMsgId, 'from', self.userId)
            self.r.hset(newMsgId, 'text', text)
            self.r.zadd(self.chatId + ':messages', {newMsgId: sTime})
            members = self.r.smembers(self.chatId+':members')
            for member in members:
                self.r.zadd(member.decode('ascii') +
                            ':chatslist', {self.chatId: sTime})

            return ShowGroupState(self.r, self.userId, self.chatId)
        if inp.startswith('MEMBERS'):
            from States.ShowMembersState import ShowMembersState
            return ShowMembersState(self.r, self.userId, self.chatId)
        if inp.startswith('BACK'):
            from States.MainPageState import MainPageState
            return MainPageState(self.r, self.userId)

        print('\n Invalid \n\n')
        return ShowGroupState(self.r, self.userId, self.chatId)
