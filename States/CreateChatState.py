from BaseState import BaseState


class CreateChatState(BaseState):
    def __init__(self, id):
        self.userId = id

    def process(self):
