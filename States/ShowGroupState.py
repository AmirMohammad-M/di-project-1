from States.BaseState import BaseState


class ShowGroupState(BaseState):
    def __init__(self, r, id):
        self.userId = id
        self.r = r

    def process(self):
        # TODO Implement group
        pass
