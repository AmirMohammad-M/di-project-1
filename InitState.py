from BaseState import BaseState


class InitState(BaseState):

    def process(self):
        phone = input('Hello. Please enter your phone number:')

        # if exists
        # return proper state
