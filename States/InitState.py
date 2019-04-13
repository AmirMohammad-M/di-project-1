from BaseState import BaseState


class InitState(BaseState):
    def __init__(self, r, userId):
        self.userId = userId
        self.r = r

    def process(self):
        phone = input('Hello. Please enter your phone number:')

        # if exists
        # return proper state
