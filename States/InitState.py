from States.BaseState import BaseState
from States.MainPageState import MainPageState


class InitState(BaseState):
    def __init__(self, r):
        self.r = r

    def process(self):
        phone = str(input('Hello. Please enter your phone number:'))
        name = self.r.hget(phone, 'name')
        if not name:
            name = input('Your name:')
            self.r.hset(phone, 'name', name)
        else:
            name = name.decode('ascii')
        print('Welcome ' + name)

        return MainPageState(self.r, phone)
