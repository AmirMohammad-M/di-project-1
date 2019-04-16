import time

from States.BaseState import BaseState


class ShowChatState(BaseState):
    def __init__(self, r, userId, chatId):
        self.userId = userId
        self.r = r
        self.chatId = chatId

    def process(self):

        print('\n\n Type SEND and start writing text you want to send.')
        print('\n Enter BACK to return to menu.\n')
        messages = self.r.zrevrange(self.chatId + ':messages', 0, 10, withscores=True)
        # othersLastSeen = int(self.r.hget(self.chatId, 'lastSeenByOthers').decode('ascii'))
        # TODO The Design for seen/new messages has problems I think...
        if len(messages) == 0:
            print('No messages.')
        else:
            for m, t in messages:
                sender = self.r.hget(m.decode('ascii'), 'from').decode('ascii')
                tab = ''
                if sender == self.userId:
                    tab = '\t\t\t'
                # else:
                #     status = '[NEW]'
                text = self.r.hget(m.decode('ascii'), 'text').decode('ascii')
                print(tab + text)  # TODO Add time from t
            else:
                if not sender == self.userId:
                    self.r.hset(self.chatId, 'lastSeenByOthers', int(time.time() * 1000))

        inp = input('\n\n> ')
        if inp.startswith('SEND '):
            sTime = int(time.time() * 1000)  # Send Time msec
            text = inp.replace('SEND ', '', 1)
            newMsgId = 'MSG' + str(sTime % (365 * 24 * 60 * 60 * 1000))
            self.r.hset(newMsgId, 'from', self.userId)
            self.r.hset(newMsgId, 'text', text)
            self.r.zadd(self.chatId + ':messages', {newMsgId: sTime})
            self.r.zadd(self.chatId.split(':')[1] + ':chatslist', {self.chatId: sTime})
            self.r.zadd(self.chatId.split(':')[2] + ':chatslist', {self.chatId: sTime})
            return ShowChatState(self.r, self.userId, self.chatId)

        if inp.startswith('BACK'):
            from States.MainPageState import MainPageState
            return MainPageState(self.r, self.userId)

        print('\n Invalid \n\n')
        return ShowChatState(self.r, self.userId, self.chatId)
