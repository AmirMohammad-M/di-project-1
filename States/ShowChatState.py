from States.BaseState import BaseState


class ShowChatState(BaseState):
    def __init__(self, r, userId):
        self.userId = userId
        self.r = r

    def process(self):
