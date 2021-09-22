from enums import InstructionStates


class Instruction:
    def __init__(self, frame, function, params=[], state=InstructionStates.IDLE):
        self.frame = frame
        self.function = function
        self.params = params
        self.state = state

    def reset(self):
        self.state = InstructionStates.IDLE

    def run(self):
        self.function(*self.params)