from States.BaseState import BaseState


class CreateGroupState(BaseState):
    def __init__(self, r, id):
        self.userId = id
        self.r = r

    def process(self):
        pass
